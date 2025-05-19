from flask import Flask, render_template
from customer import Customer
from coffee import Coffee

app = Flask(__name__)

# Create some example data (like in your debug.py)
alice = Customer("Alice")
bob = Customer("Bob")

latte = Coffee("Latte")
espresso = Coffee("Espresso")

alice.create_order(latte, 4.5)
alice.create_order(espresso, 3.0)
bob.create_order(latte, 5.0)
bob.create_order(latte, 4.0)

@app.route('/')
def index():
    # Pass your data to the template
    customers = [alice, bob]
    coffees = [latte, espresso]
    return render_template('index.html', customers=customers, coffees=coffees)

if __name__ == '__main__':
    app.run(debug=True)
