import MySql_Conn


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
                
    print(MySql_Conn.mycursor.rowcount, "record inserted.")
