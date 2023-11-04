import datetime

import pytest

from database import BaseModel, Order
from database.models import OrderType
from database.session import SessionManager


@pytest.fixture(scope='session')
def session_manager():
    session_manager = SessionManager(
        db_dsn='sqlite+pysqlite:///:memory:',
        echo=True,
    )
    BaseModel.metadata.drop_all(session_manager.engine)
    BaseModel.metadata.create_all(session_manager.engine)
    return session_manager


@pytest.fixture
def db_session(session_manager):
    session = session_manager.get_session()
    yield session
    session.rollback()
    session.close()


def test_order(db_session):
    """Test Order creation."""
    order = Order(
        order_type=OrderType.BUY,
        quantity=5,
        price=18.99,
    )
    db_session.add(order)
    db_session.flush()
    assert order.id is not None
    assert order.order_type.value == 'buy'
    assert order.quantity == 5
    assert float(order.price) == 18.99
    assert order.timestamp.date() == datetime.date.today()
