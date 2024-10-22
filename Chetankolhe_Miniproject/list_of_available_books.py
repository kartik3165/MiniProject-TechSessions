import MySql_Conn

def display_available_books():
    sql2 = "SELECT book_id,book_name from books where book_status = 'Available'"
    MySql_Conn.mycursor.execute(sql2)
    myresult = MySql_Conn.mycursor.fetchall()
    print("\nList of Available Books are:- ")
    for i in myresult:
        if(i!='None'):
            print(i)
    print("\n")