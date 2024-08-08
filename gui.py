/* HERE IS GUI FILE */

import tkinter as tk
from tkinter import simpledialog
from products import add_product, update_product, delete_product, get_products

def main():
    root = tk.Tk()
    root.title("Inventory Management System")

    def show_products():
        products = get_products()
        product_list.delete(0, tk.END)
        for product in products:
            product_list.insert(tk.END, f"{product[0]}: {product[1]} - {product[2]} units - ${product[3]}")

    def add_product_gui():
        name = simpledialog.askstring("Input", "Product Name:")
        quantity = simpledialog.askinteger("Input", "Quantity:")
        price = simpledialog.askfloat("Input", "Price:")
        if name and quantity is not None and price is not None:
            add_product(name, quantity, price)
            show_products()

    def delete_product_gui():
        product_id = simpledialog.askinteger("Input", "Product ID to delete:")
        if product_id is not None:
            delete_product(product_id)
            show_products()

    tk.Button(root, text="Show Products", command=show_products).pack()
    tk.Button(root, text="Add Product", command=add_product_gui).pack()
    tk.Button(root, text="Delete Product", command=delete_product_gui).pack()

    product_list = tk.Listbox(root, width=50, height=10)
    product_list.pack()

    root.mainloop()
