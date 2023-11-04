import datetime
import enum

from decimal import Decimal

from sqlalchemy import DECIMAL

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class BaseModel(DeclarativeBase):
    """Basic class for models."""
    id: Mapped[int] = mapped_column(
        primary_key=True,
    )


class OrderType(enum.Enum):
    """Order types."""
    BUY = 'buy'
    SELL = 'sell'


class Order(BaseModel):
    """Order model."""
    __tablename__ = 'orders'

    order_type: Mapped[OrderType]
    quantity: Mapped[int]
    price: Mapped[Decimal] = mapped_column(DECIMAL(precision=8, scale=2))

    timestamp: Mapped[datetime.datetime] = mapped_column(
        default=datetime.datetime.now(),
    )

    def __repr__(self) -> str:
        return (
            f"Order("
            f"id={self.id}, "
            f"order_type={self.order_type}, "
            f"price={self.price})"
        )
