"""
We can use TypedDict to implement Data Transfer Object that is typed and can be compared (implements __eq__).

advantages:
- can provide typing to existing dictionaries
- being still a dictionary, can map to JSON data structures

disadvantages:
- only available from Python 3.8
- not immutable
- doesn't support default values
- all defined keys have to exist in the dictionary
"""
import sys
from typing import TypedDict
from models import Invoice, Order


class InvoiceOrderDto(TypedDict):
    invoice: Invoice
    order: Order
    message: str


def return_dto() -> InvoiceOrderDto:
    invoice = Invoice(1)
    order = Order(1)
    # return {"invoice": invoice, "order": order, "message": message='default message'} -> Also possible
    # return InvoiceOrderDto(invoice=invoice, order=order) -> Fails type check
    return InvoiceOrderDto(invoice=invoice, order=order, message='default message')


dto = return_dto()

print(sys.getsizeof(dto))
# -> 232

print(dto)
# -> {'invoice': Invoice(id=1), 'order': Order(id=1), 'message': 'default message'}

for key in dto.keys():
    print(key, dto[key])
# -> invoice Invoice(id=1)
#    order Order(id=1)
#    message default message

dto2 = return_dto()
print(dto == dto2)
# -> True