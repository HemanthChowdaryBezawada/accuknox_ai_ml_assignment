import csv
import sqlite3

with open('users.csv', 'r') as file:
    reader = csv.DictReader(file)
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    """)
    for row in reader:
        cursor.execute("""
            INSERT INTO users (name, email) VALUES (?, ?)
        """, (row['Name'], row['Email']))
    connection.commit()
    connection.close()