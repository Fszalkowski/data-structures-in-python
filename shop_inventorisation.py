import sqlite3

#connect with database
connection = sqlite3.connect("shop.db") 
cursor = connection.cursor()

#createing new tables
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
        product_price = float(input("Enter product price(PLN): "))
        product_stock_quantity = int(input("Enter how many product you have on stock: "))

        cursor.execute('''
            INSERT INTO products (name, price, stock_quantity)
            VALUES (?, ?, ?)
        ''', (product_name, product_price, product_stock_quantity))
        
        while True:
            querry_1 = input("You wanna add another product? (yes/no)").strip().lower()
            if querry_1 == "yes":
                continue
            elif querry_1 == "no":
                break
            else:
                print("Invalid value. Please enter 'yes' or 'no'. ")
                break
    except ValueError:
        print("Enter values one more.")
        continue

    try:
        customer_name = input("Enter customer name: ")
        customer_email = input("Enter customer e-mail adress: ")

        cursor.execute('''
            INSERT INTO products (name, emial)
            VALUES (?, ?)
        ''', (customer_name, customer_email))

    except ValueError:
        print("Enter values one more.")
        continue
    break

print("Sucess.")

connection.commit()
connection.close()

#inprogress