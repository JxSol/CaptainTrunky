import pytest
from sqlalchemy import select

from database.models import Order, BaseModel, OrderType
from database.repositories import OrderBook
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


def test_connection(db_session):
    """Test if connection established."""
    assert db_session.is_active


def test_order_book(db_session):
    """Test OrderBook repository."""
    order_book = OrderBook(db_session)
    order = order_book.add(
        {
            'order_type': OrderType.BUY,
            'quantity': 28,
            'price': 18.99,
        },
    )
    order_book.commit()
    order_id = order.id
    assert order_id is not None

    order = order_book.get_order(order_id)
    assert isinstance(order, Order)

    orders = order_book.get_orders()
    assert isinstance(orders, list)
    assert len(orders) > 0

    order_book.modify(order_id, {'quantity': 43, 'foo': 'bar'})
    order_book.commit()
    order = db_session.get(Order, order_id)
    assert order.quantity == 43

    order_book.delete(order_id)
    order_book.commit()
    order = db_session.get(Order, order_id)
    assert order is None

    db_session.add(
        Order(
            order_type=OrderType.BUY,
            quantity=66,
            price=20,
        )
    )
    db_session.add(
        Order(
            order_type=OrderType.SELL,
            quantity=73,
            price=10,
        )
    )
    db_session.commit()
    order_book.match()
    order = db_session.execute(
        select(Order)
        .where(Order.quantity == 73)
    ).one_or_none()
    assert order is None
