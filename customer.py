# customer.py

class Customer:
    def __init__(self, name):
        self.name = name  # Triggers the @name.setter validation
        self._orders = []

    @property
    def name(self):
        return self._name  

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string.")
        if not (1 <= len(value) <= 15):
            raise ValueError("Name must be between 1 and 15 characters.")
        self._name = value

    def add_order(self, order):
        """Add an Order instance to this customer."""
        self._orders.append(order)

    def orders(self):
        """Return all Order instances for this customer."""
        return self._orders

    def coffees(self):
        """Return a unique list of Coffee instances the customer has ordered."""
        return list({order.coffee for order in self._orders})

    def __repr__(self):
        return f"Customer('{self.name}')"
