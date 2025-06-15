import sqlite3
import random
import os
from datetime import datetime, timedelta

def init_database():
    # Create data directory if it doesn't exist
    os.makedirs('data', exist_ok=True)
    
    # Connect to SQLite database
    db_path = os.path.join('data', 'ecommerce.db')
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    
    # Create tables
    with open('schema.sql') as f:
        c.executescript(f.read())
    
    # Insert sample customers
    customers = [
        ('Anushka ', 'anushkag23@gmail.com', 'SouthExtension'),
        ('Rishi', 'rishi_04@gmail.com', 'GK-2'),
        ('Diksha', 'diksha#28@gmail.com', 'Gurgaon'),
        ('Anmol', 'anmol_10@gmail.com', 'Gurgaon'),
        ('Daksh Gaur', 'daksh10@gmail.com', 'Gurgaon')
    ]
    
    # Insert sample products
    products = [
        ('Laptop', 999.99),
        ('Smartphone', 699.99),
        ('Tablet', 399.99),
        ('Headphones', 199.99),
        ('Monitor', 299.99)
    ]
    
    for customer in customers:
        c.execute("INSERT INTO customers (name, email, city) VALUES (?, ?, ?)", customer)
    
    for product in products:
        c.execute("INSERT INTO products (name, price) VALUES (?, ?)", product)
    
    # Create orders with random data
    cities = ['New Delhi ', 'Gurgaon', 'SouthExtension', 'GK-2']
    for _ in range(30):
        cust_id = random.randint(1, len(customers))
        prod_id = random.randint(1, len(products))
        quantity = random.randint(1, 5)
        order_date = (datetime.now() - timedelta(days=random.randint(0, 90))).strftime('%Y-%m-%d')
        c.execute(
            "INSERT INTO orders (customer_id, product_id, quantity, order_date) VALUES (?, ?, ?, ?)",
            (cust_id, prod_id, quantity, order_date)
        )
    
    conn.commit()
    conn.close()
    print(f"Database initialized successfully at {db_path}")

if __name__ == '__main__':
    init_database()