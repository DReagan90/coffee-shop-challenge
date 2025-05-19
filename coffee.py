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
        return self._name  # Immutable

    def add_order(self, order):
        """Add an Order instance to this coffee."""
        self._orders.append(order)

    def orders(self):
        """Return all Order instances for this coffee."""
        return self._orders

    def customers(self):
        """Return a unique list of Customer instances who ordered this coffee."""
        return list({order.customer for order in self._orders})

    def num_orders(self):
        """Return the total number of orders for this coffee."""
        return len(self._orders)

    def average_price(self):
        """Return the average price of all orders for this coffee."""
        if not self._orders:
            return 0
        total = sum(order.price for order in self._orders)
        return total / len(self._orders)

    def __repr__(self):
        return f"Coffee('{self.name}')"
