import random

from database.models import OrderType, BaseModel
from database.repositories import OrderBook
from database.session import SessionManager


class MarketSimulator:
    """Simulate a market."""

    def __init__(self, session_manager, iterations: int = 50):
        self.session_manager = session_manager
        self.iterations = iterations
        self.repository = OrderBook(session_manager.get_session())
        self.simulate()

    @staticmethod
    def get_random_order_data():
        data = {
            'order_type': random.choice((OrderType.BUY, OrderType.SELL)),
            'quantity': random.randint(1, 999),
            'price': random.randint(1, 999) + round(random.random(), 2),
        }
        return data

    def simulate(self):
        for _ in range(self.iterations):
            self.repository.add(self.get_random_order_data())
            self.repository.commit()
            if random.random() > 0.66:
                self.repository.match()
        print('Simulation is over.')


if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        i = int(sys.argv[1])
    else:
        i = 50

    session_manager = SessionManager(
        db_dsn='sqlite:///order_book.sqlite3',
        echo=False,
    )
    BaseModel.metadata.drop_all(session_manager.engine)
    BaseModel.metadata.create_all(session_manager.engine)
    MarketSimulator(session_manager, i)
