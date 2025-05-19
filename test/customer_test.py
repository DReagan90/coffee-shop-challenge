import unittest
from customer import Customer
from coffee import Coffee

class TestCustomer(unittest.TestCase):

    def test_valid_name(self):
        c = Customer("Alice")
        self.assertEqual(c.name, "Alice")

    def test_invalid_name(self):
        with self.assertRaises(ValueError):
            Customer("")  
        with self.assertRaises(ValueError):
            Customer("A" * 16)  
        with self.assertRaises(ValueError):
            Customer(123)  

    def test_create_order_and_coffees(self):
        c = Customer("Bob")
        coffee = Coffee("Latte")
        c.create_order(coffee, 3.5)
        self.assertEqual(len(c.orders()), 1)
        self.assertIn(coffee, c.coffees())
