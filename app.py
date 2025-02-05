from flask import Flask, jsonify, request

app = Flask(__name__)

books = [
    {"id": 1, "title": "1984", "author": "George Orwell", "published_year": 1949},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee", "published_year": 1960},
    {"id": 3, "title": "Thez Great Gatsby", "author": "F. Scott Fitzgerald", "published_year": 1925},
]

@app.route('/books', methods=['GET'])
def get_books():
    # Look for an "author" query parameter in the request
    author_query = request.args.get("author")
    print (author_query)
    if author_query:
        # Filter books by matching the query against the "author" field (case-insensitive)
        filtered_books = [
            book for book in books
            if author_query.lower() in book["author"].lower()
        ]
        return jsonify({"books": filtered_books})
    return jsonify({"books": books})

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book["id"] == book_id), None)
    if book:
        return jsonify(book)
    return jsonify({"error": "Book not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)