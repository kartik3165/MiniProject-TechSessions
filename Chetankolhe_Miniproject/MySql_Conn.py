
import mysql.connector

#this file connect my sql to python
mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="1234",
  database="lib_management"
)
mycursor = mydb.cursor()