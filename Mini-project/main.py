import mysql.connector
from datetime import datetime 
import time

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="admin",
  database="lib"
)

def Add_student():
    # student id will auto genrate
    name = input("Enter student name : ")
    dept = input("Enter student department : ")
    fine = 0

    mycursor = mydb.cursor()
    query = "INSERT INTO students VALUES (%s , %s , %s)"
    data = (name , dept , fine)
    mycursor.execute(query,data)
    mydb.commit()
    print("Student added!")

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
            query ="UPDATE students SET student_name = %s WHERE student_id = %s"
            value = (new_name , data[0])
            change.execute(query,value)
            mydb.commit()
            print("Name update") 
        elif update_ch == 2: # change name
            new_dept = input("Enter new dept : ")
            change = mydb.cursor()
            query ="UPDATE students SET student_dept = %s WHERE student_id = %s"
            value = (new_dept , data[0])
            change.execute(query,value)
            mydb.commit()
            print("Dept update") 

def Add_book():
    b_id = int(input("Enter unique book id : "))
    title = input("Enter your book title : ")
    author = input("Enter author name : ")
    total_copies = int(input("Number of copy : "))
    available_copies = total_copies

    add = mydb.cursor()
    query = "INSERT INTO books VALUES (%s, %s , %s , %s , %s)"
    data = (b_id , title , author , total_copies , available_copies)
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
        print(f"\n Book id : {data[0]}\n Title : {data[1]}\n Author : {data[2]}\n Total Copies : {data[3]}\n Available Copies : {data[4]}")
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
            query ="UPDATE books SET total_copies = %s WHERE book_id = %s"
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
    
def Issue_book():
    issue_id = None
    student_id = int(input("Enter register student id : "))
    book_id = int(input("Enter register book id : "))
    issue_date = datetime.today() # yyyy/mm/dd
    i = time.localtime()
    issue_time = time.strftime("%H:%M",i)
    due_date = None
    return_date = None
    return_time = None
    status = "issued"

def late_fine():
    fine_id = None
    issue_id = None
    fine_amount = None
    paid_status = None
