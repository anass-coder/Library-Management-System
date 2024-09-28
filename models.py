class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
        self.borrowed_books = []

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True