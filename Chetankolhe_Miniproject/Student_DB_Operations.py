
import MySql_Conn
def insert_student(stud_id,stud_name,stud_class):

    sql = "INSERT INTO student (stud_id,stud_name,stud_class,stud_zprn,penalty,issue_status) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (stud_id,stud_name,stud_class,"122E18030",0,"Not Issued")

    MySql_Conn.mycursor.execute(sql, val)
    MySql_Conn.mydb.commit()
    print("\n")
    print(MySql_Conn.mycursor.rowcount, " Student Record Inserted !!!\n")
    
def update_student(student):
    
    
    choice = int(input("\n Select Choice :- \n"
                       "1.Update Name\n2.Update ZPRN\n3.Update Class\n 4.EXIT :- \n"))
    
    while(True):
        if(choice == 1):
            input_stud_name = input("Enter the new name of student :- ")
            sql_stud = "UPDATE student SET stud_name = %s where stud_id = %s "
            val_stud = (input_stud_name , student)
            MySql_Conn.mycursor.execute(sql_stud, val_stud)
            MySql_Conn.mydb.commit()
            print(" \nName Updated Succesfully !!!\n")
            
        elif(choice == 2):
            input_stud_ZPRN = input("Enter the new ZPRN of student :- ")
            sql_stud = "UPDATE student SET stud_zprn = %s where stud_id = %s "
            val_stud = (input_stud_ZPRN , student)
            MySql_Conn.mycursor.execute(sql_stud, val_stud)
            MySql_Conn.mydb.commit()
            print(" \nZPRN Updated Succesfully !!!\n")
            
        elif(choice == 3):
            input_stud_class = input("Enter the new Class of student :- ")
            sql_stud = "UPDATE student SET stud_class = %s where stud_id = %s "
            val_stud = (input_stud_class , student)
            MySql_Conn.mycursor.execute(sql_stud, val_stud)
            MySql_Conn.mydb.commit()
            print(" \nClass Updated Succesfully !!!\n")
            
        elif(choice == 4):
            break
            
        else:
            print("\nInvaild Choice !!!\n Enter Correct Choice \n")


def delete_student(stud_id):
    
    sql_stud = "DELETE FROM student where stud_id = %s"
    val_stud = (stud_id,)
    MySql_Conn.mycursor.execute(sql_stud, val_stud)
    MySql_Conn.mydb.commit()
    print("\n Student Record Deleted succesfully \n")
    
def display_stud_record():
    sql2 = "SELECT * from student"
    # MySql_Conn.mycursor.execute(sql, val)
    print(MySql_Conn.mycursor.execute(sql2))
    myresult = MySql_Conn.mycursor.fetchall()
    for i in myresult:
        print(i)
