import MySql_Conn
def penalty_pay(stud_id):
    sql_penalty = "UPDATE student SET penalty = 0 WHERE stud_id = %s AND penalty != 0;"
    val_penalty = ([int(digit) for digit in str(stud_id)])


    check_penalty = "SELECT penalty from student where stud_id = %s "
    check_val_penalty =([int(digit) for digit in str(stud_id)])
    MySql_Conn.mycursor.execute(check_penalty , check_val_penalty)
    penalty= MySql_Conn.mycursor.fetchone()

    if(penalty[0]!=0):
        
        MySql_Conn.mycursor.execute(sql_penalty, val_penalty)
        MySql_Conn.mydb.commit()
        print(f"\nPenalty of INR {penalty[0]} Paid Successfully\n")
        
    elif(penalty[0]==0):
        print("\nNothing To Pay\n")
        


