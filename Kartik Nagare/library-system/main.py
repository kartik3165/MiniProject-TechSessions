import mysql.connector
from datetime import datetime , timedelta , date

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="admin",
  database="lib"
)

def Add_student():
    # student id will auto genrate
    id = int(input("Enter id : "))
    name = input("Enter student name : ")
    dept = input("Enter student department : ")
    fine = 0.0

    mycursor = mydb.cursor()
    query = "INSERT INTO students VALUES (%s , %s , %s , %s)"
    data = (id , name , dept , fine )
    mycursor.execute(query,data)
    mydb.commit()
    print("Student added")

def Update_student(prn):
    mycursor = mydb.cursor()
    mycursor.execute(f"SELECT * FROM students WHERE student_id = {prn}")
    result = mycursor.fetchall()
    data = []
    for i in result: # give list to iterate it 
        for j in i:  # give tuple to iterate it 
            data.append(j) # create new list to acess the row get from 
    
    if prn == data[0]:
        print("Current info")
        print(f"Student id : {data[0]}\n Student name : {data[1]}\n student dept : {data[2]}\n")
        print("1.Update Name\n2.Update Dept")
        update_ch = int(input("Enter your operation : "))

        if update_ch == 1: # change name
            new_name = input("Enter new name : ")
            change = mydb.cursor()
            query ="UPDATE students SET name = %s WHERE student_id = %s"
            value = (new_name , data[0])
            change.execute(query,value)
            mydb.commit()
            print("Name update") 
        elif update_ch == 2: # change name
            new_dept = input("Enter new dept : ")
            change = mydb.cursor()
            query ="UPDATE students SET dept = %s WHERE student_id = %s"
            value = (new_dept , data[0])
            change.execute(query,value)
            mydb.commit()
            print("Dept update") 

def Add_book():
    b_id = int(input("Enter unique book id : "))
    title = input("Enter your book title : ")
    author = input("Enter author name : ")
    total_copies = int(input("Number of copy : "))
    book_price = int(input("Enter book price : "))

    add = mydb.cursor()
    query = "INSERT INTO books VALUES (%s, %s , %s , %s , %s )"
    data = (b_id , title , author , total_copies , book_price)
    add.execute(query,data)
    mydb.commit()
    print("Book added")

def Update_book(id):
    update = mydb.cursor()
    update.execute(f"SELECT * FROM books WHERE book_id = {id}")
    result = update.fetchall()
    data = []
    for i in result:
        for j in i:
            data.append(j)
    
    if id == data[0]:
        print("Current book information")
        print(f"\n Book id : {data[0]}\n Title : {data[1]}\n Author : {data[2]}\n Total Copies : {data[3]}")
        print("\n1.Update title\n2.Author\n3.total copies")
        update_ch = int(input("Enter your operation : "))

        if update_ch == 1:
            new = input("Enter new title : ")
            change = mydb.cursor()
            query ="UPDATE books SET title = %s WHERE book_id = %s"
            value = (new , data[1])
            change.execute(query,value)
            mydb.commit()
            print("Title update") 
        elif update_ch == 2:
            new = input("Enter new author : ")
            change = mydb.cursor()
            query ="UPDATE books SET author = %s WHERE book_id = %s"
            value = (new , data[2])
            change.execute(query,value)
            mydb.commit()
            print("Author update")
        elif update_ch == 3:
            new = int(input("Enter new author : "))
            change = mydb.cursor()
            query ="UPDATE books SET quantity = %s WHERE book_id = %s"
            value = (new , data[3])
            change.execute(query,value)
            mydb.commit()
            print("Copies update")

def Delete_book(id):
    delete = mydb.cursor()
    query = "DELETE FROM books WHERE book_id = %s"
    value = (id)
    delete.execute(query,value)
    mydb.commit()
    print("Book deleted")

def get_BookData(id):
    # 0 for book_id
    # 1 for title
    # 2 for author
    # 3 for quantity
    getData = mydb.cursor()
    getData.execute(f"SELECT * FROM books WHERE book_id = {id}")
    result = getData.fetchall()
    book = []
    for i in result:
        for j in i:
            book.append(j)
    return book

def get_studentData(id):
    # 0 for student_id
    # 1 for name
    # 2 for dept
    # 3 for fine
    getData = mydb.cursor()
    getData.execute(f"SELECT * FROM Students WHERE student_id = {id}")
    result = getData.fetchall()
    student = []
    for i in result:
        for j in i:
            student.append(j)
    return student

def get_IssuebookData(id):
    # 0 for issue_id     1 for student_id
    # 2 for book_id      3 for issue_date
    # 4 for due_date     5 for return_date
    getData = mydb.cursor()
    getData.execute(f"SELECT * FROM Issued_Books WHERE issue_id = {id}")
    result = getData.fetchall()
    issueBook = []
    for i in result:
        for j in i:
            issueBook.append(j)
    return issueBook

def get_LostbookData(id):
    # 0 for lost_id     1 for issue_id
    # 2 for lost_date   3 for fine_amount
    getData = mydb.cursor()
    getData.execute(f"SELECT * FROM Lost_Books WHERE lost_id = {id}")
    result = getData.fetchall()
    lostBook = []
    for i in result:
        for j in i:
            lostBook.append(j)
    return lostBook

def Issue_book():
    issue_id = int(input("Enter Issued ID: "))  
    student_id = int(input("Enter registered student ID: "))
    book_id = int(input("Enter registered book ID: "))
    issue_date = datetime.now().date()
    issue_date_str = issue_date.strftime('%Y-%m-%d')
    due_date = issue_date + timedelta(days=7)
    due_date_str = due_date.strftime('%Y-%m-%d')  # Format the due date
    return_date = None  

    issue = mydb.cursor()
    query = "INSERT INTO Issued_Books (issue_id, student_id, book_id, issue_date, due_date, return_date, fine) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    data = (issue_id, student_id, book_id, issue_date_str, due_date_str, return_date, fine)
    issue.execute(query, data)

    #update book quantity
    current_quantity = get_BookData(book_id)
    updated_quantity =  current_quantity[0] - 1
    q2 = "UPDATE Books SET quantity = %s WHERE book_id = %s"
    d2 = (updated_quantity , book_id)

    issue.execute(q2, d2)
    mydb.commit()
    print("Book Issued")

def Lost_Books():
    lost_id = int(input("Enter lost id : "))
    issue_id = int(input("Enter registered book id :"))
    lost_date = datetime.now().date()
    lost_date_str = lost_date.strftime('%Y-%m-%d')
    book_id = get_IssuebookData(issue_id)[2]
    student_id = get_IssuebookData(book_id)[1]
    book_price = get_BookData(book_id)[4]
    fine_amount = book_price
    current_fine = get_studentData(student_id)[3]

    lost = mydb.cursor()
    query = "INSERT INTO Lost_Books VALUES (%s , %s , %s , %s , %s)"
    data = (lost_id , issue_id , lost_date_str , fine_amount)
    lost.execute(query , data)

    # Add fine to issued_book
    updated_fine = current_fine + fine_amount
    q2 = "UPDATE Students SET fine = %s WHERE student_id = %s"
    d2 = (updated_fine , student_id)
    lost.execute(q2 , d2)

    mydb.commit()
    print("fine added")

def DateDifference(d1, d2):
    d0_input = str(d1)
    while len(d0_input) != 10 or d0_input[4] != '-' or d0_input[7] != '-':
        print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
        d0_input = d1
    d0 = date.fromisoformat(d0_input)  

    d1_input = str(d2)
    while len(d1_input) != 10 or d1_input[4] != '-' or d1_input[7] != '-':
        print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
        d1_input = d2
    d1 = date.fromisoformat(d1_input) 

    delta = d1 - d0
    return delta.days

def Return_Book(id):
    issue_id = int(input("Enter book issue id : "))
    issue_date = get_IssuebookData(issue_id)[3]
    due_date = get_IssuebookData(issue_id)[4]
    return_date = get_IssuebookData(issue_id)[5]
    student_id = get_IssuebookData(issue_id)[1]
    book_id = get_IssuebookData(issue_id)[2]
    book_quantity = get_BookData(book_id)[0]

    date_difference = DateDifference(f"{issue_date}" , f"{return_date}")
    current_fine = get_studentData(student_id)[3]
    
    back = mydb.cursor()
    if date_difference > 7:
        fine = (date_difference - 7) * 2 # per day 2rs fine
        print(fine)
        q2 = "UPDATE Students SET fine = %s WHERE student_id = %s" 
        d2 = (fine , student_id)

    # book quantity update
    updated_book_quantity = book_quantity + 1
    q1 = "UPDATE Books SET quantity = %s WHERE book_id = %s"
    d1 = (updated_book_quantity , book_id)
    back.execute(q1,d1)
    back.execute(q2,d2)
    mydb.commit()
    print(f"Book submited with fine {fine}.")
    


while True:
    print("\n--- Library Management System ---")
    print("1. Add Student")
    print("2. Update Student")
    print("3. Add Book")
    print("4. Update Book")
    print("5. Delete Book")
    print("6. Issue Book")
    print("7. Return Book")
    print("8. Report Lost Book")
    print("9. Exit")

    choice = input("Enter your choice (1-9): ")

    if choice == '1':
        Add_student()
    elif choice == '2':
        prn = int(input("Enter student ID to update: "))
        Update_student(prn)
    elif choice == '3':
        Add_book()
    elif choice == '4':
        book_id = int(input("Enter book ID to update: "))
        Update_book(book_id)
    elif choice == '5':
        book_id = int(input("Enter book ID to delete: "))
        Delete_book(book_id)
    elif choice == '6':
        Issue_book()
    elif choice == '7':
        Return_Book()
    elif choice == '8':
        Lost_Books()
    elif choice == '9':
        print("Exiting the system.")
        break
    else:
        print("Invalid choice. Please select a valid option.")

