from sqlalchemy import select
from sqlalchemy.orm import Session

from .models import Order, OrderType


class OrderBook:
    """Repository for Orders."""
    model: Order = Order

    def __init__(self, session: Session):
        self.session = session

    def get_order(self, order_id: int) -> model:
        """Get an Order."""
        order = self.session.get(self.model, order_id)
        return order

    def get_orders(self) -> list[model]:
        """Get list of all orders."""
        stmt = select(self.model)
        orders = list(self.session.execute(stmt).all())
        return orders

    def add(self, data: dict) -> model:
        """Add a new Order."""
        order = Order(**data)
        self.session.add(order)
        self.session.flush()
        return order

    def modify(self, order_id: int, data: dict) -> model:
        """Modify an existing Order."""
        order = self.session.get(self.model, order_id)
        for field, value in data.items():
            if hasattr(order, field):
                setattr(order, field, value)
        self.session.flush()
        return order

    def delete(self, order_id: int) -> None:
        """Remove an Order."""
        order = self.session.get_one(self.model, order_id)
        self.session.delete(order)
        self.session.flush()

    def commit(self) -> None:
        """Commit changes."""
        self.session.commit()

    def match(self) -> None:
        """Find the matching Order."""
        stmt_buy = (
            select(self.model)
            .where(self.model.order_type == OrderType.BUY)
            .order_by(self.model.price.desc())
            .limit(1)
        )
        best_buy = self.session.execute(stmt_buy).scalar()

        stmt_sell = (
            select(self.model)
            .where(self.model.order_type == OrderType.SELL)
            .order_by(self.model.price.asc())
            .limit(1)
        )
        best_sell = self.session.execute(stmt_sell).scalar()

        if best_buy and best_sell and best_buy.price > best_sell.price:
            print(
                f"Seller: {best_sell} "
                f"| Buyer: {best_buy} "
                f"| Difference: {best_buy.price - best_sell.price}"
            )
            self.delete(best_buy.id)
            self.delete(best_sell.id)
            self.session.commit()
