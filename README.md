
# Coffee Shop Challenge

A simple Flask web application simulating a coffee shop system with Customers, Coffees, and Orders.

---

## Features

- Manage Customers and Coffees.
- Customers can place orders for different coffees with specified prices.
- Track orders associated with customers and coffees.
- Display orders, customers, and coffees on a web interface.
- Identify the customer who is the biggest fan ("most aficionado") of a particular coffee.

---

## Project Structure
coffee-shop-challenge/
├── app.py # Flask app entry point
├── customer.py # Customer class definition
├── coffee.py # Coffee class definition
├── order.py # Order class definition
├── templates/
│ └── index.html # Main HTML template for the homepage
├── README.md # Project documentation


---

## Setup & Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/coffee-shop-challenge.git
   cd coffee-shop-challenge
2. Create and activate a virtual environment:

       python3 -m venv venv
       source venv/bin/activate    # On Windows: venv\Scripts\activate
3. Install dependencies:

       pip install -r requirements.txt
4. Start the Flask development server:

       flask run

 Usage
The homepage displays the list of customers and coffees.

Customers and coffees can be extended by modifying the Python classes.

Orders can be created programmatically or by extending the Flask app with forms.


