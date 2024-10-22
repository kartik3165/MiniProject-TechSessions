import MySql_Conn
from datetime import datetime

def Issue_book(book_id,stud_id):
    
    check_b_id = "SELECT book_id from books"
    MySql_Conn.mycursor.execute(check_b_id)
    myresult_id = MySql_Conn.mycursor.fetchall()
    
    book_ids = [row[0] for row in myresult_id]
    #here checking if the book_id entered is in our data base or not
    if book_id in book_ids:
    
        now = datetime.now()
        issue_date = now.strftime('%Y-%m-%d %H:%M:%S')

        return_date = None
        return_status = "Pending"
                    
        #fetching stud_name form the student data base
        check1 = "SELECT stud_name from student where stud_id = %s "
        check_val1 =([int(digit) for digit in str(stud_id)])
        MySql_Conn.mycursor.execute(check1 , check_val1)
        myresult1 = MySql_Conn.mycursor.fetchone()
        stud_name = myresult1[0]

        sql = "INSERT INTO issued_book_info (book_id,book_issuedby_stud_id,stud_name,issued_date,return_date,return_status) VALUES ( %s, %s,%s, %s, %s, %s)"
        val = (book_id,stud_id,stud_name,issue_date,return_date,return_status)


        #update query to change the book_status
        sql_update = "UPDATE  books SET book_status = 'Not Available' where book_id = %s "
        val_update = ([int(digit) for digit in str(book_id)])

        #update query to update the Issue status of student
        sql_student = "UPDATE  student SET issue_status = 'Issued' where stud_id = %s "
        val_student = ([int(digit) for digit in str(stud_id)])

        #checking if the book exisist or not      
        check = "SELECT book_id,book_status from books where book_id = %s "
        check_val =([int(digit) for digit in str(book_id)])
        MySql_Conn.mycursor.execute(check , check_val)
        myresult = MySql_Conn.mycursor.fetchone()
    
    
    
        #checking if the student has alread issued any book or not    
        check_student = "SELECT issue_status from student where stud_id = %s "
        check_val_student =([int(digit) for digit in str(stud_id)])
        MySql_Conn.mycursor.execute(check_student , check_val_student)
        myresult_student = MySql_Conn.mycursor.fetchone()


        if(myresult[0] == book_id and myresult[1]=="Available" and myresult_student[0]=="Not Issued"):
            
            # update  query for book table
            MySql_Conn.mycursor.execute(sql_update, val_update)
            MySql_Conn.mydb.commit()
            
            # update  query for student table
            MySql_Conn.mycursor.execute(sql_student, val_student)
            MySql_Conn.mydb.commit()
            
            
            #for insert query in issued book details table
            MySql_Conn.mycursor.execute(sql, val)
            MySql_Conn.mydb.commit()
            # MySql_Conn.mycursor.rowcount, 
            print(f"\nBook Number {book_id} Issued By {stud_name} Stud_ID Number {stud_id} \n")
            
            
        elif(myresult[1]=="Not Available"):
            print("\nBook Is Not Available For Issue\n")
            
        elif(myresult_student[0]=="Issued"):
            print("\nThis Student has Already Issued A Book\nReturn the Issued Book first\n")
            
        else:
            print("\nBook ID Does Not exists\n")
    
    else:
        print("\nBook iD Entered Is Not Valid OR Book Is Not Available\n")
            

                    

