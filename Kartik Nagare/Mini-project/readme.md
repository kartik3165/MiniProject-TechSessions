
# Library Management System

A simple Library Management System built using **Python** and **MySQL**, with version control via **Git** and hosted on **GitHub**.

## Resource
https://medium.com/@qemhal.h/different-ways-to-display-a-table-in-python-d867aefb624a
https://www.programiz.com/python-programming/datetime/current-time

## Features

### 1. Manage Student
- **Add Student**: Register new students in the system.
- **Update Student**: Modify student information.

### 2. Manage Book
- **Add Book**: Add new books to the library inventory.
- **Update Book**: Edit details of existing books.
- **Delete Book**: Remove books from the inventory.

### 3. Book Issue
- Issue books to students, ensuring only **available** books can be issued.

### 4. Return Book / Lost Book
- **Return Book**: Accept returned books and update availability.
- **Lost Book**: Mark books as lost and handle necessary updates.

### 5. Penalty Management
- **Calculate Penalty**: Automatically compute penalties for:
  - **Late Returns**: Penalty for returning books after the due date.
  - **Lost Books**: Add a fixed penalty for lost books to the student's account.

## Tech Stack
- **Python**: Core programming language.
- **MySQL**: Database for storing student and book records.
- **Git & GitHub**: Version control and collaboration.

---

# Library Management System Database Schema

## 1. Students Table
Stores student information and tracks total fines.

| Field          | Type             | Null | Key  | Default      | Extra          |
|----------------|------------------|------|------|--------------|----------------|
| student_id     | INT              | NO   | PRI  | NULL         | AUTO_INCREMENT |
| student_name   | VARCHAR(100)     | NO   |      | NULL         |                |
| student_dept   | VARCHAR(100)     | NO   |      | NULL         |                |
| total_fine     | DECIMAL(10, 2)   | YES  |      | 0.00         |                |

## 2. Books Table
Stores book information including the number of available copies.

| Field              | Type             | Null | Key  | Default      | Extra          |
|--------------------|------------------|------|------|--------------|----------------|
| book_id            | INT              | NO   | PRI  | NULL         | AUTO_INCREMENT |
| title              | VARCHAR(255)     | NO   |      | NULL         |                |
| author             | VARCHAR(255)     | YES  |      | NULL         |                |
| total_copies       | INT              | YES  |      | 1            |                |
| available_copies   | INT              | YES  |      | 1            |                |

## 3. Issued Books Table
Tracks issued books, returns, and lost books, including fines.

| Field          | Type             | Null | Key  | Default      | Extra          |
|----------------|------------------|------|------|--------------|----------------|
| issue_id       | INT              | NO   | PRI  | NULL         | AUTO_INCREMENT |
| student_id     | INT              | YES  | MUL  | NULL         |                |
| book_id        | INT              | YES  | MUL  | NULL         |                |
| issue_date     | DATE             | YES  |      | NULL         |                |
| due_date       | DATE             | YES  |      | NULL         |                |
| return_date    | DATE             | YES  |      | NULL         |                |
| status         | ENUM('issued', 'returned', 'lost') | YES | | 'issued'    |                |
| fine_amount    | DECIMAL(10, 2)   | YES  |      | 0.00         |                |

## 4. Late Fines Table
Tracks fines for late returns.

| Field          | Type             | Null | Key  | Default      | Extra          |
|----------------|------------------|------|------|--------------|----------------|
| fine_id        | INT              | NO   | PRI  | NULL         | AUTO_INCREMENT |
| issue_id       | INT              | YES  | MUL  | NULL         |                |
| fine_amount    | DECIMAL(10, 2)   | YES  |      | NULL         |                |
| paid_status    |ENUM(paid,'unpaid)| YES  |      | 'unpaid'     |                |
