import unittest
from coffee import Coffee
from customer import Customer

class TestCoffee(unittest.TestCase):

    def test_valid_name(self):
        coffee = Coffee("Espresso")
        self.assertEqual(coffee.name, "Espresso")

    def test_invalid_name(self):
        with self.assertRaises(ValueError):
            Coffee("AB")  
        with self.assertRaises(ValueError):
            Coffee(123)  

    def test_average_price_and_num_orders(self):
        coffee = Coffee("Mocha")
        c1 = Customer("Amy")
        c2 = Customer("Tom")
        c1.create_order(coffee, 5.0)
        c2.create_order(coffee, 7.0)
        self.assertEqual(coffee.num_orders(), 2)
        self.assertAlmostEqual(coffee.average_price(), 6.0)
