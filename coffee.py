# coffee.py

class Coffee:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        if len(name) < 3:
            raise ValueError("Name must be at least 3 characters long.")
        self._name = name
        self._orders = []

    @property
    def name(self):
        return self._name

    def add_order(self, order):
        """Add an Order instance to this coffee."""
        self._orders.append(order)

    def orders(self):
        """Return all Order instances for this coffee."""
        return self._orders

    def customers(self):
        """Return a unique list of Customer instances who ordered this coffee."""
        return list({order.customer for order in self._orders})

    def __repr__(self):
        return f"Coffee('{self.name}')"
