"""
Example of model classes (typically subclassed, managed by ORM, etc.)
"""


class Invoice:
    id: int

    def __init__(self, id: int):
        self.id = id

    def __repr__(self):
        return f"Invoice(id={self.id})"

    def __eq__(self, other):
        return self.id == other.id


class Order:
    id: int

    def __init__(self, id: int):
        self.id = id

    def __repr__(self):
        return f"Order(id={self.id})"

    def __eq__(self, other):
        return self.id == other.id