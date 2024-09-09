# Project Plan: Library Management System

## 1. Project Title:
**Library Management System**

## 2. Project Description:
This project aims to create a database-driven Library Management System (LMS) to manage books, borrowers, and transactions efficiently. The database will allow librarians to track the availability of books, manage borrower details, and log the issuance and return of books.

## 3. Objective:
- To develop an easy-to-manage database system to keep track of:
  - Books (title, author, genre, availability, etc.)
  - Borrowers (name, contact info, borrowed books, etc.)
  - Transactions (check-out, return, overdue fines)
  
- Implement basic CRUD operations for managing books and borrowers.
  
- Lay the foundation for future expansions such as online book reservations.

## 4. Entities and Relationships:
### Entities:
- **Book**: (ID, title, author, genre, availability)
- **Borrower**: (ID, name, contact info, email)
- **Transaction**: (transaction ID, borrower ID, book ID, issue date, return date, fine)

### Relationships:
- A borrower can borrow multiple books.
- A book can be borrowed by one borrower at a time.
- Each transaction logs a book’s borrowing and returning.

## 5. Technologies:
- **Database**: MySQL (for relational database management)
- **Backend**: Python with MySQL Connector
- **Optional Frontend**: HTML interface

