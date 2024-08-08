/*HERE IS THE DATABASE FILE*/

import sqlite3

def execute_query(query, params=()):
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    cursor.execute(query, params)
    conn.commit()
    conn.close()

def fetch_query(query, params=()):
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    cursor.execute(query, params)
    results = cursor.fetchall()
    conn.close()
    return results

def create_db():
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        quantity INTEGER NOT NULL,
        price REAL NOT NULL
    )
    '''
    execute_query(create_table_query)

def add_product(name, quantity, price):
    """Add a new product."""
    query = 'INSERT INTO products (name, quantity, price) VALUES (?, ?, ?)'
    execute_query(query, (name, quantity, price))

def update_product(product_id, name, quantity, price):
    """Update an existing product."""
    query = 'UPDATE products SET name = ?, quantity = ?, price = ? WHERE id = ?'
    execute_query(query, (name, quantity, price, product_id))

def delete_product(product_id):
    """Delete a product."""
    query = 'DELETE FROM products WHERE id = ?'
    execute_query(query, (product_id,))

def get_products():
    """Get all products."""
    query = 'SELECT * FROM products'
    return fetch_query(query)
