
## Resource use to solve error
https://medium.com/@qemhal.h/different-ways-to-display-a-table-in-python-d867aefb624a

https://www.programiz.com/python-programming/datetime/current-time

https://stackoverflow.com/questions/14625191/error-code-1292-incorrect-date-value-mysql

https://www.tutorialspoint.com/change-date-format-in-mysql-database-table-to-d-m-y

https://www.tutorialspoint.com/How-do-I-calculate-number-of-days-between-two-dates-using-Python

# Library Management System

This is a simple Library Management System built using Python and MySQL to manage books, students, and book transactions (such as issuing and returning books). The system also handles lost books and fines for late submissions.

## Features

- **Add, Update, and Delete Books**
- **Add and Manage Students**
- **Issue Books to Students**
- **Return Books and Handle Late Fines**
- **Manage Lost Books and Lost Book Fines**

## Database Schema

The system uses a relational database with four tables: `Books`, `Students`, `Issued_Books`, and `Lost_Books`. The schema ensures that each operation, such as issuing or losing a book, is properly tracked with foreign key relationships to maintain data integrity.

### Tables

#### 1. `Books`
This table stores all the book details in the library.

| Column         | Data Type        | Description                        |
|----------------|------------------|------------------------------------|
| `book_id`      | INT              | Primary Key, Auto Increment        |
| `title`        | VARCHAR(255)     | Title of the book                  |
| `author`       | VARCHAR(255)     | Author of the book                 |
| `quantity`     | INT              | Number of copies available         |
| `book_price`   | INT              | Price of book
#### 2. `Students`
This table stores information about students who borrow books from the library.

| Column         | Data Type        | Description                        |
|----------------|------------------|------------------------------------|
| `student_id`   | INT              | Primary Key, Auto Increment         |
| `name`         | VARCHAR(255)     | Name of the student                |
| `dept`         | VARCHAR(255)     | Department of the student          |
| `fine`         | DECIMAL(5, 2)    | Fine for late return (default 0.00)|

#### 3. `Issued_Books`
This table tracks which books have been issued to which students.

| Column         | Data Type        | Description                        |
|----------------|------------------|------------------------------------|
| `issue_id`     | INT              | Primary Key, Auto Increment         |
| `student_id`   | INT              | Foreign Key, references `Students`  |
| `book_id`      | INT              | Foreign Key, references `Books`     |
| `issue_date`   | DATE             | Date when the book was issued      |
| `due_date`     | DATE             | Date by which the book should be returned |
| `return_date`  | DATE             | Date when the book was returned (nullable) |

#### 4. `Lost_Books`
This table records details of books that have been reported lost by students.

| Column         | Data Type        | Description                        |
|----------------|------------------|------------------------------------|
| `lost_id`      | INT              | Primary Key, Auto Increment         |
| `issue_id`     | INT              | Foreign Key, references `Issued_Books` |
| `lost_date`    | DATE             | Date when the book was reported lost |
| `fine_amount`  | DECIMAL(6, 2)    | Fine imposed for the lost book     |

