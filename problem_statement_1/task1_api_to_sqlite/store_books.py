import sqlite3
from fetch_books import fetch_books

def db_connect(db_path="books.db"):
    connection = sqlite3.connect(db_path)
    return connection

def books_table(connection):
    cursor = connection.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS books(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            author TEXT,
            publish_year INTEGER,
            language TEXT
        )"""
    )

def insert_books(connection, books):
    cursor = connection.cursor()
    for book in books:
        cursor.execute(
            """INSERT INTO books (title, author, publish_year, language)
            VALUES(?, ?, ?, ?)""",
            (
                book["title"],
                book["author"],
                book["publish_year"],
                book["language"]
            )
        )

books = fetch_books()

connection = db_connect()
books_table(connection)
insert_books(connection, books)

connection.commit()
cursor = connection.cursor()
cursor.execute("SELECT * FROM books")

books_data = cursor.fetchall()
for book in books_data:
    print(book)
connection.close()

print("Books have been successfully fetched and stored in the database.")