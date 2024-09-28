from datetime import date
import sqlite3
import json

def setup_database():
    # Connect to (or create) the SQLite database
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()

    # Create the books table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            isbn TEXT NOT NULL,
            availability BOOLEAN,
            serialized_state TEXT  -- To store additional serialized information if needed
        )
    ''')

# Create the borrowers table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS borrowers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            borrowed_books TEXT,  -- JSON string to store borrowed book IDs
            serialized_state TEXT  -- To store additional serialized information if needed
        )
    ''')

    conn.commit()
    conn.close()


# Add a new book (Placeholders for later implementation)
def add_book(title, author, isbn, availability=True):
    """Add a book to the database."""
    book_data = {
        'title': title,
        'author': author,
        'isbn': isbn,
        'availability': availability
    }
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    
    # Insert book data into the table
    cursor.execute(
        "INSERT INTO books (title, author, isbn, availability, serialized_state) VALUES (?, ?, ?, ?, ?)",
        (title, author, isbn, availability, json.dumps(book_data))
    )

    conn.commit()
    conn.close()

# View all books (Placeholders for later implementation)
def view_books():
    """Retrieve all books from the database."""
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()

    conn.close()
    return books

# Add a new borrower (Placeholders for later implementation)
def add_borrower(name, email, borrowed_books=None):
    """Add a borrower to the database."""
    if borrowed_books is None:
        borrowed_books = []

    borrower_data = {
        'name': name,
        'email': email,
        'borrowed_books': borrowed_books
    }

    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    
    # Insert borrower data into the table
    cursor.execute(
        "INSERT INTO borrowers (name, email, borrowed_books, serialized_state) VALUES (?, ?, ?, ?)",
        (name, email, json.dumps(borrower_data['borrowed_books']), json.dumps(borrower_data))
    )

    conn.commit()
    conn.close()

def list_borrowers():
    """Retrieve all borrowers from the database."""
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM borrowers")
    borrowers = cursor.fetchall()

    conn.close()
    return borrowers    

# Borrow a book (Placeholders for later implementation)
def borrow_book():
    # TODO: Write code to log the borrowing of a book in the 'Transaction' table
    pass

# Return a book (Placeholders for later implementation)
def return_book():
    # TODO: Write code to update the return date in the 'Transaction' table
    pass

# View all transactions (Placeholders for later implementation)
def view_transactions():
    # TODO: Write code to fetch and display all transactions
    pass
