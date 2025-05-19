from customer import Customer
from coffee import Coffee
from order import Order

alice = Customer("Alice")
bob = Customer("Bob")

latte = Coffee("Latte")
espresso = Coffee("Espresso")


alice.create_order(latte, 4.5)
alice.create_order(espresso, 3.0)
bob.create_order(latte, 5.0)
bob.create_order(latte, 4.0)


print("Alice's Orders:")
for order in alice.orders():
    print(f"- {order.coffee.name}: ${order.price}")

print("\nBob's Coffees:")
for coffee in bob.coffees():
    print(f"- {coffee.name}")


print(f"\n{latte.name} has {latte.num_orders()} orders")
print(f"Average price for {latte.name}: ${latte.average_price():.2f}")


most_loyal = Customer.most_aficionado(latte)
if most_loyal:
    print(f"\nMost aficionado for {latte.name}: {most_loyal.name}")
else:
    print(f"\nNo orders yet for {latte.name}")
