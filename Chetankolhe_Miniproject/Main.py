import MySql_Conn
from datetime import datetime
import penalty_payment
import Issue_book
import list_of_available_books
import Student_DB_Operations
import Book_DB_Operations

while(True):
    choice = int(input("Enter the Choice\n"
                    "1.Insert New Books\n"
                    "2.Delete Existing Books\n"
                    "3.Add New Student\n"
                    "4.Upate Existing Student data\n"
                    "5.Delete Existing Student Data\n"
                    "6.Display All Available Books\n"
                    "7.Issue a Book\n"
                    "8.Return a Book\n"
                    "9.Penalty Payment\n"
                    "10.Exit\n"
                    ))
    
    if(choice == 1):
        #just calling the function in file insertion_of_book_in_db
        Book_DB_Operations.book_insert()
    
    elif(choice == 2):
        book_id = int(input("Enter the id of student whose data you want to delete :- "))
        
        Book_DB_Operations.delete_book(book_id)
    
    
    elif(choice == 3):
        
        #taking the information as an input to insert new data
        stud_id = int(input("Enter the student ID number :- "))
        stud_name = input("Enter thr name of student :- ")
        stud_class = input("Enter the class of student :- ")
        
        #just calling the function insert_student in the file student_DB_Operation
        Student_DB_Operations.insert_student(stud_id,stud_name,stud_class)
        
    elif(choice == 4):
        
        #taking the stud_id as an input to update student data
        student = int(input("\nEnter the id of student whose data you want to update :- "))\
            
        check_s_id = "SELECT stud_id from student"
        MySql_Conn.mycursor.execute(check_s_id)
        myresult_id = MySql_Conn.mycursor.fetchall()
        
        #here checking if the stud_id entered is in our data base or not
        if student in myresult_id:
            
            #just calling the function in the file name Student_DB_Operations
            Student_DB_Operations.update_student(student)
        
        else:
            print("\nStudent Not Exisist !!\nREcheck Your Entered ID \n")
        
        
    elif(choice == 5):
        
        stud_id = int(input("\nEnter the id of student whose data you want to Delete :- "))
        
        check_s_id = "SELECT stud_id from student"
        MySql_Conn.mycursor.execute(check_s_id)
        myresult_id = MySql_Conn.mycursor.fetchall()
        
        #here checking if the stud_id entered is in our data base or not
        if stud_id in myresult_id:
            Student_DB_Operations.delete_student(stud_id)
        else:
            print("\nStudent Not Exisist !!\nREcheck Your Entered ID \n")
        
    elif(choice == 6):
         #just calling the function in file insertion_of_book_in_db
        list_of_available_books.display_available_books()
        
        
    elif(choice == 7):
        book_id = int(input("Enter the Book Id "))
        stud_id = input("\nEnter the id of student:- ")
        #calling the Function in issued_book_info file
        Issue_book.Issue_book(book_id,stud_id)

    elif(choice == 8):
        book_id = int(input("Enter the Book Id "))
        stud_id = input("\nEnter the id of student:- ")
        #calling the Function in return_book file
        Book_DB_Operations.book_return(book_id,stud_id)
        
        
    elif(choice == 9):
        
       
        stud_id = input("\nEnter the id of student:- ")
        
        check_s_id = "SELECT stud_id from student"
        MySql_Conn.mycursor.execute(check_s_id)
        myresult_id = MySql_Conn.mycursor.fetchall()
        
        #here checking if the stud_id entered is in our data base or not
        if stud_id in myresult_id:
            #calling the Function in penalty_payment file 
            penalty_payment.penalty_pay(stud_id)
        else:
            print("\nStudent Not Exisist !!\nREcheck Your Entered ID \n")
        
    elif(choice == 10):
        print("Thankyou !!!")
        break
    
    else:
        print("Enter The Valid Choice\n"
              "Choice Entered is Invalid")
    