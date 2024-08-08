/* HERE IS THE PRODUCTS FILE */

from database import execute_query, fetch_query

def add_product(name, quantity, price):
    execute_query('INSERT INTO products (name, quantity, price) VALUES (?, ?, ?)', (name, quantity, price))

def update_product(product_id, name, quantity, price):
    execute_query('UPDATE products SET name = ?, quantity = ?, price = ? WHERE id = ?', (name, quantity, price, product_id))

def delete_product(product_id):
    execute_query('DELETE FROM products WHERE id = ?', (product_id,))

def get_products():
    return fetch_query('SELECT * FROM products')
