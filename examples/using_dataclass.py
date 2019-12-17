"""
We can use @dataclass to implement Data Transfer Object that is immutable, typed,
, supports default values and can be compared (implements __eq__).

advantages:
- configurable if necessary (repr, eq, frozen)
"""
import sys
from dataclasses import dataclass
from models import Invoice, Order


@dataclass(frozen=True)
class InvoiceOrderDto():
    invoice: Invoice
    order: Order
    message: str = "default message"


def return_dto() -> InvoiceOrderDto:
    invoice = Invoice(1)
    order = Order(1)
    return InvoiceOrderDto(invoice, order)


dto = return_dto()

print(sys.getsizeof(dto))
# -> 64

print(dto)
# -> InvoiceOrderDto(invoice=Invoice(id=1), order=Order(id=1), message='default message')

for i in dto:
    print(i)
# -> TypeError: 'InvoiceOrderDto' object is not iterable

dto.invoice = Invoice(2)
# -> dataclasses.FrozenInstanceError: cannot assign to field 'invoice'

dto2 = return_dto()
print(dto == dto2)
# -> True