from datetime import datetime
import MySql_Conn

#function to insert book in the database
def book_insert():
    book_id = int(input("Enter the Book Id "))
    book_name = input("\nEnter the Name Of Book:- ")
    book_authar= input(f"\nEnter the Author of Book {book_name}:- ")
    book_year = int(input(f"\nEnter the year of publish of {book_name}:- "))
    book_status = "Available"
                
    sql = "INSERT INTO books (book_id,book_name,book_Author,book_year,book_status) VALUES ( %s, %s, %s, %s, %s)"
    val = (book_id,book_name,book_authar,book_year,book_status)
                
    MySql_Conn.mycursor.execute(sql, val)
    MySql_Conn.mydb.commit()
    print("\n")
    print(MySql_Conn.mycursor.rowcount, " Book inserted Succesfully !!! \n")

#function to delete book from the data base
def delete_book(book_id):
    
    
    sql_stud = "DELETE FROM books where book_id = %s"
    val_stud = (book_id,)
    MySql_Conn.mycursor.execute(sql_stud, val_stud)
    MySql_Conn.mydb.commit()
    print("\n1 Book Deleted succesfully !!!\n")


#function to calculate the total penalty applied
def penalty_cal(stud_id):
    check_penalty = "SELECT issued_date,return_date from issued_book_info where book_issuedby_stud_id = %s "
    check_val_penalty =([int(digit) for digit in str(stud_id)])
    MySql_Conn.mycursor.execute(check_penalty , check_val_penalty)
    date= MySql_Conn.mycursor.fetchone()
    
    issued_date, return_date = date
    
    # is_date=date[0]
    # re_date=date[1]
    # temp=str(re_date - is_date)
    # temp2=temp.split()
    # diff = int(temp2[0])
    
    diff = (return_date - issued_date).days

    if(diff > 7):
        total_penalty = (diff-7)*10
        penalty = "UPDATE student SET penalty = %s where stud_id = %s "
        peanlty_val = (total_penalty,stud_id) 
        MySql_Conn.mycursor.execute(penalty, peanlty_val)
        MySql_Conn.mydb.commit()
        print(f"\nBook Returned Successfully\n"
            f"A penalty of INR {total_penalty} must be paid within the next 7 days.\n"
            "Otherwise, you will not be able to issue another book.\n")

        
    elif(diff>0 and diff<7):
        print("\nBook returned on time. No penalty applied. Thank you!\n")

        
#function to return the borrowed book
def book_return(book_id,stud_id):
    now = datetime.now()
    return_date = now.strftime('%Y-%m-%d %H:%M:%S')


    #update the return status in issued_book_info table
    #to_give_example    return date '2024-11-09'
    sql = "UPDATE issued_book_info SET return_status = 'Returned Successfully',return_date = %s where book_issuedby_stud_id = %s and book_id= %s and return_status = 'Pending' "
    val = (return_date,stud_id,book_id)


    #update the studeent issue status
    sql_stud = "UPDATE student SET issue_status = 'Not Issued' where stud_id = %s "
    val_stud = ([int(digit) for digit in str(stud_id)])


    #update the book status
    sql_book = "UPDATE books SET book_status = 'Available' where book_id = %s "
    val_book = ([int(digit) for digit in str(book_id)])


    #fetching stud_name form the student data base
    check1 = "SELECT issue_status from student where stud_id = %s "
    check_val1 =([int(digit) for digit in str(stud_id)])
    MySql_Conn.mycursor.execute(check1 , check_val1)
    myresult1 = MySql_Conn.mycursor.fetchone()
    issue_status = myresult1[0]


    #checking if the student has issued book or not 
    #if student not issued any book he/she can't return the bookh
    if(issue_status == "Issued"):
        
        MySql_Conn.mycursor.execute(sql, val)
        MySql_Conn.mycursor.execute(sql_stud, val_stud)
        MySql_Conn.mycursor.execute(sql_book, val_book)
        MySql_Conn.mydb.commit()
        
        penalty_cal(stud_id)
        print("\nBook Returned Successfully !!! \n")
        
    elif(issue_status == "Not Issued"):
        print("\nNo Book is issued by the student currently\n")
        


    
