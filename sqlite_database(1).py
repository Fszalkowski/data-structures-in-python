import sqlite3
connection = sqlite3.connect("my_database.db")
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
''')
connection.commit()

while True:
    try:
        user_name = input("Enter your name: ")
    except ValueError:
        print("Invalid value!")
        continue
    break

cursor.execute('''
    INSERT INTO users (name) 
    VALUES (?)
''', (user_name,))
connection.commit()

print("Users: ")
cursor.execute('SELECT name FROM users')
rows = cursor.fetchall()

for row in rows:
    print(row[0])

connection.close()
