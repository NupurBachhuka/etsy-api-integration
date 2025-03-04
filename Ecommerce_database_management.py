import mysql.connector
from tkinter import *
from tkinter import ttk, simpledialog, messagebox
import requests    # For Etsy API

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="nuka1421",
    database="Ecommerce_database_management"
)
cursor = con.cursor()

def execute_query(query, values=None, fetch=False):
    cursor.execute(query, values or ())
    if fetch:
        return cursor.fetchall()
    con.commit()

execute_query("""
CREATE TABLE IF NOT EXISTS customer (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_name VARCHAR(255),
    gender VARCHAR(10),
    address TEXT,
    phone_no VARCHAR(15),
    cart_num INT UNIQUE
);
""")
execute_query("""
CREATE TABLE IF NOT EXISTS product (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    product_name VARCHAR(255),
    price DECIMAL(10,2),
    stock INT
);
""")
execute_query("""
CREATE TABLE IF NOT EXISTS cart_item (
    cart_id INT AUTO_INCREMENT PRIMARY KEY,
    cart_no INT,
    product_no INT,
    quantity INT,
    FOREIGN KEY (cart_no) REFERENCES customer(cart_num),
    FOREIGN KEY (product_no) REFERENCES product(product_id)
);
""")

# Tkinter for frontend 
root = Tk()
root.title("E-Commerce Database Management")

# Customer Management Section
Label(root, text="Customer Details").grid(row=0, column=0, columnspan=2)
Label(root, text="Name:").grid(row=1, column=0)
entry_customer_name = Entry(root)
entry_customer_name.grid(row=1, column=1)
Label(root, text="Gender:").grid(row=2, column=0)
entry_gender = Entry(root)
entry_gender.grid(row=2, column=1)
Label(root, text="Address:").grid(row=3, column=0)
entry_address = Entry(root)
entry_address.grid(row=3, column=1)
Label(root, text="Phone No:").grid(row=4, column=0)
entry_phone_no = Entry(root)
entry_phone_no.grid(row=4, column=1)
Label(root, text="Cart No:").grid(row=5, column=0)
entry_cart_num = Entry(root)
entry_cart_num.grid(row=5, column=1)

def add_customer():
    query = "INSERT INTO customer (customer_name, gender, address, phone_no, cart_num) VALUES (%s, %s, %s, %s, %s)"
    values = (entry_customer_name.get(), entry_gender.get(), entry_address.get(), entry_phone_no.get(), entry_cart_num.get())
    execute_query(query, values)
    messagebox.showinfo("Success", "Customer added successfully!")

Button(root, text="Add Customer", command=add_customer).grid(row=6, column=0, columnspan=2)

# Product Selection Section
Label(root, text="Select Product").grid(row=7, column=0, columnspan=2)
dropdown = ttk.Combobox(root)
dropdown.grid(row=8, column=0, columnspan=2)

sample_products = [
    # Electronics
    ("Laptop", 999.99, 10), ("Smartphone", 599.99, 20), ("Headphones", 199.99, 15),
    ("Smartwatch", 299.99, 8), ("Tablet", 450.00, 12), ("Wireless Earbuds", 129.99, 25),
    ("Gaming Console", 499.99, 6), ("Mechanical Keyboard", 89.99, 30), ("Monitor 24-inch", 199.99, 18),
    ("External Hard Drive", 79.99, 22), ("Graphics Card", 699.99, 5), ("Bluetooth Speaker", 149.99, 20),

    # Home Appliances
    ("Microwave Oven", 179.99, 12), ("Air Purifier", 249.99, 9), ("Coffee Maker", 89.99, 20),
    ("Electric Kettle", 39.99, 30), ("Vacuum Cleaner", 299.99, 7), ("Air Fryer", 149.99, 12),
    ("Refrigerator", 999.99, 5), ("Washing Machine", 699.99, 4), ("Dishwasher", 799.99, 6),

    # Fashion & Clothing
    ("Leather Jacket", 129.99, 15), ("Running Shoes", 89.99, 20), ("Smart Glasses", 249.99, 10),
    ("Denim Jeans", 59.99, 25), ("Woolen Sweater", 49.99, 30), ("Sports Watch", 149.99, 18),
    ("Handbag", 199.99, 12), ("Sunglasses", 79.99, 22), ("Sneakers", 99.99, 14),

    # Beauty & Health
    ("Organic Face Cream", 29.99, 35), ("Hair Straightener", 59.99, 15), ("Perfume", 89.99, 20),
    ("Makeup Kit", 99.99, 18), ("Massage Gun", 149.99, 10), ("Electric Toothbrush", 49.99, 25),
    ("Skincare Set", 79.99, 15), ("Lipstick Set", 39.99, 30), ("Essential Oil Set", 29.99, 22),

    # Furniture
    ("Office Chair", 199.99, 10), ("Standing Desk", 299.99, 8), ("Wooden Dining Table", 499.99, 5),
    ("Sofa Set", 799.99, 3), ("Bed Frame", 599.99, 6), ("Bookshelf", 199.99, 10),
    ("Nightstand", 99.99, 12), ("Wardrobe", 699.99, 4), ("Folding Chair", 39.99, 20),

    # Toys & Games
    ("Board Game Set", 49.99, 15), ("RC Car", 129.99, 10), ("Dollhouse", 199.99, 8),
    ("Lego Set", 89.99, 12), ("Puzzle Set", 29.99, 30), ("Action Figure", 19.99, 40),
    ("Gaming Headset", 79.99, 20), ("VR Headset", 399.99, 7), ("Drone", 899.99, 3),

    # Books & Stationery
    ("Notebook Pack", 19.99, 50), ("Gel Pen Set", 9.99, 100), ("Art Supplies Kit", 39.99, 25),
    ("E-Reader", 129.99, 12), ("Fiction Novel", 24.99, 30), ("Cookbook", 29.99, 15),
    ("Planner Journal", 19.99, 40), ("Desk Lamp", 49.99, 20), ("Smart Notebook", 79.99, 10),

    # Sports & Outdoors
    ("Camping Tent", 149.99, 5), ("Trekking Backpack", 99.99, 10), ("Yoga Mat", 29.99, 30),
    ("Dumbbell Set", 59.99, 15), ("Cycling Helmet", 39.99, 20), ("Basketball", 19.99, 50),
    ("Fishing Rod", 89.99, 12), ("Hiking Shoes", 109.99, 8), ("Tennis Racket", 69.99, 15),

    # Automotive & Tools
    ("Car Vacuum Cleaner", 49.99, 18), ("Dash Cam", 99.99, 12), ("Jump Starter", 129.99, 8),
    ("Tool Kit", 79.99, 15), ("Cordless Drill", 139.99, 10), ("Car Seat Cover Set", 79.99, 20),
    ("Tire Inflator", 59.99, 25), ("Portable Generator", 499.99, 4), ("Motorcycle Helmet", 149.99, 12),

    # Pet Supplies
    ("Dog Bed", 69.99, 15), ("Cat Scratching Post", 49.99, 20), ("Pet Grooming Kit", 39.99, 30),
    ("Automatic Pet Feeder", 89.99, 10), ("Bird Cage", 119.99, 8), ("Aquarium Kit", 149.99, 5),
    ("Dog Training Pads", 29.99, 40), ("Pet Carrier Bag", 79.99, 12), ("Rabbit Hutch", 129.99, 6)
]

for product in sample_products:
    query = "INSERT INTO product (product_name, price, stock) VALUES (%s, %s, %s)"
    execute_query(query, product)

def populate_dropdown():
    products = execute_query("SELECT product_id, product_name FROM product", fetch=True)
    dropdown['values'] = [f"{row[0]} - {row[1]}" for row in products]

def add_to_cart():
    selected_product = dropdown.get()
    if not selected_product:
        messagebox.showerror("Error", "Please select a product")
        return
    product_id = selected_product.split('-')[0].strip()
    cart_num = entry_cart_num.get()
    quantity = simpledialog.askinteger("Quantity", f"Enter quantity for {selected_product}")
    if quantity:
        query = "INSERT INTO cart_item (cart_no, product_no, quantity) VALUES (%s, %s, %s)"
        execute_query(query, (cart_num, product_id, quantity))
        messagebox.showinfo("Success", "Product added to cart!")

Button(root, text="Load Products", command=populate_dropdown).grid(row=9, column=0, columnspan=2)
Button(root, text="Add to Cart", command=add_to_cart).grid(row=10, column=0, columnspan=2)

# Etsy API Integration (Waiting for Key Approval)
#i am still waiting for my etsy api key to get approved, or the time being i have populated the product table with sample products
#once the key gets approved this database managemnet system will directly interact with ETSY's database to get details about products lsitings and other stuff
# def fetch_etsy_products():
#     API_KEY = "MY api key"  
#     url = "https://api.etsy.com/v3/application/shops/My shop id/listings/active"
#     headers = {"Authorization": f"Bearer {API_KEY}"}
#     response = requests.get(url, headers=headers)
#     if response.status_code == 200:
#         products = response.json()
#         for product in products["results"]:
#             query = "INSERT INTO product (product_id, product_name, price, stock) VALUES (%s, %s, %s, %s)"
#             values = (product["listing_id"], product["title"], product["price"], product["quantity"])
#             execute_query(query, values)
#         messagebox.showinfo("Success", "Etsy products fetched successfully!")
#     else:
#         messagebox.showerror("Error", "Failed to fetch Etsy products")

Button(root, text="Fetch Etsy Data (Pending Approval)", command=lambda: messagebox.showinfo("Etsy API", "Etsy API integration will be enabled once the key is approved.")).grid(row=11, column=0, columnspan=2)

root.mainloop()
