from dataclasses import dataclass, field
from enum import Enum


class Status(Enum):
    PENDING = "pending"
    PAID = "paid"
    SHIPPED = "shipped"
    CANCELLED = "cancelled"


@dataclass
class Customer:
    id: int
    email: str
    name: str


@dataclass
class Product:
    id: int
    sku: str
    price_cents: int


@dataclass
class OrderItem:
    product: Product
    quantity: int

    def total_cents(self) -> int:
        return self.product.price_cents * self.quantity


@dataclass
class Order:
    id: int
    customer: Customer
    status: Status = Status.PENDING
    items: list[OrderItem] = field(default_factory=list)

    def total_cents(self) -> int:
        return sum(item.total_cents() for item in self.items)

    def pay(self) -> None:
        self.status = Status.PAID
