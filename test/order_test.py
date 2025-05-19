import unittest
from order import Order
from customer import Customer
from coffee import Coffee

class TestOrder(unittest.TestCase):

    def test_valid_order(self):
        customer = Customer("Lana")
        coffee = Coffee("Cappuccino")
        order = Order(customer, coffee, 4.5)
        self.assertEqual(order.customer, customer)
        self.assertEqual(order.coffee, coffee)
        self.assertEqual(order.price, 4.5)

    def test_invalid_order(self):
        with self.assertRaises(ValueError):
            Order(Customer("Joe"), Coffee("Latte"), 0.5)  
        with self.assertRaises(TypeError):
            Order("Joe", Coffee("Latte"), 3.0) 
        with self.assertRaises(TypeError):
            Order(Customer("Joe"), "Latte", 3.0)  
