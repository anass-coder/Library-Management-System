import mysql.connector
from datetime import date

# MySQL connection configuration
db = mysql.connector.connect(
    host="localhost",
    user="root",  # MySQL username
    password="yourpassword",  # MySQL password
    database="library_management"  #the database 
)

cursor = db.cursor()

# Add a new book (Placeholders for later implementation)
def add_book():
    # TODO: Write code to insert a new book into the 'Book' table
    pass

# View all books (Placeholders for later implementation)
def view_books():
    # TODO: Write code to fetch and display all books from the 'Book' table
    pass

# Add a new borrower (Placeholders for later implementation)
def add_borrower():
    # TODO: Write code to insert a new borrower into the 'Borrower' table
    pass

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

# Menu to interact with the system (Placeholders for the CRUD functions)
def menu():
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. View All Books")
        print("3. Add Borrower")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. View All Transactions")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_book()  # Call the add_book function
        elif choice == '2':
            view_books()  # Call the view_books function
        elif choice == '3':
            add_borrower()  # Call the add_borrower function
        elif choice == '4':
            borrow_book()  # Call the borrow_book function
        elif choice == '5':
            return_book()  # Call the return_book function
        elif choice == '6':
            view_transactions()  # Call the view_transactions function
        elif choice == '7':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the menu
if __name__ == "__main__":
    menu()
