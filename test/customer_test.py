from customer import Customer
from coffee import Coffee

def test_customer_name_validation():
    try:
        Customer("A" * 16)
        assert False, "Should raise ValueError for long names"
    except ValueError:
        pass

    c = Customer("Alice")
    assert c.name == "Alice"
