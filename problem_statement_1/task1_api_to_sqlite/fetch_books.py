import requests

def fetch_books():
    API_URL = "https://openlibrary.org/search.json?q=science+fiction&limit=10"
    HEADERS = {"User-Agent": "accuknox-assignment/1.0"}

    response = requests.get(API_URL, headers=HEADERS)

    response.raise_for_status()

    data = response.json()

    books = []

    for doc in data["docs"]:
        book = {
            "title": doc.get("title"), 
            "author": ",".join(doc.get("author_name", [])) or None,
            "publish_year": doc.get("first_publish_year"),
            "language": ",".join(doc.get("language", [])) or None,
        }
        books.append(book)

    return books
