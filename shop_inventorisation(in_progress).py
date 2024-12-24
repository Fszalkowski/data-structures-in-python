import sqlite3

#connect with database
connection = sqlite3.connect("shop.db") 
cursor = connection.cursor()

#createing new tables if not exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL NOT NULL,
        stock_quantity INTEGER NOT NULL
    )
''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL
    )
''')

#adding inventorisation products
while True:
    try:
        product_name = input("Enter name of your product: ")
        product_price = float(input("Enter product price (PLN): "))
        if product_price <= 0:
            print("Price must be greater than zero.")
            continue
        product_stock_quantity = int(input("Enter how many products you have in stock: "))
        if product_stock_quantity < 0:
            print("Stock quantity cannot be negative.")
            continue

        cursor.execute('''
            INSERT INTO products (name, price, stock_quantity)
            VALUES (?, ?, ?)
        ''', (product_name, product_price, product_stock_quantity))

        # Ask if user wants to add another product
        add_another = input("Do you want to add another product? (yes/no): ").strip().lower()
        if add_another != "yes":
            break
    except ValueError:
        print("Invalid input. Please enter the correct values.")
        continue

#customer adding
while True:
    try:
        customer_name = input("Enter customer name: ")
        customer_email = input("Enter customer email address: ")
        if not is_valid_email(customer_email):
            print("Invalid email address. Please enter a valid email.")
            continue

        cursor.execute('''
            INSERT INTO customers (name, email)
            VALUES (?, ?)
        ''', (customer_name, customer_email))

        add_another_customer = input("Do you want to add another customer? (yes/no): ").strip().lower()
        if add_another_customer != "yes":
            break
    except ValueError:
        print("Invalid input. Please enter the correct values.")
        continue

print("Sucess.")

connection.commit()
connection.close()

#inprogress
