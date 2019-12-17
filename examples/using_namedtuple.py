"""
We can use NamedTuple to implement Data Transfer Object that is immutable, typed,
, supports default values and can be compared (implements __eq__).

advantages:
- iterable

disadvantages:
- fields with a default value must come after any fields without a default
"""
import sys
from typing import NamedTuple
from models import Invoice, Order


class InvoiceOrderDto(NamedTuple):
    invoice: Invoice
    order: Order
    message: str = "default message"


def return_dto() -> InvoiceOrderDto:
    invoice = Invoice(1)
    order = Order(1)
    return InvoiceOrderDto(invoice, order)


dto = return_dto()

print(sys.getsizeof(dto))
# -> 80

print(dto)
# -> InvoiceOrderDto(invoice=Invoice(id=1), order=Order(id=1), message='default message')

for i in dto:
    print(i)
# -> Invoice(id=1)
#    Order(id=1)
#    default message

dto.invoice = Invoice(2)
# -> AttributeError: can't set attribute

dto2 = return_dto()
print(dto == dto2)
# -> True