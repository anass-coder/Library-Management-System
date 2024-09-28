from datetime import date
import sqlite3
from db_operations import *

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
    setup_database()
    menu()
