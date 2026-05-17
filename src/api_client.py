import urllib.request
import urllib.parse
import json


def search_books(query: str, limit: int = 5) -> list[dict]:
    """Search books on Open Library API by query string."""
    encoded = urllib.parse.quote(query)
    url = f"https://openlibrary.org/search.json?q={encoded}&limit={limit}"

    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            data = json.loads(response.read().decode("utf-8"))
    except OSError as e:
        raise ConnectionError(f"Não foi possível conectar à Open Library API: {e}") from e

    books = []
    for doc in data.get("docs", []):
        books.append({
            "title": doc.get("title", "Título desconhecido"),
            "authors": doc.get("author_name", ["Autor desconhecido"]),
            "year": doc.get("first_publish_year"),
        })
    return books
