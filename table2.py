#table2 for sale
import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',passwd='',db='electronicshop')
mycursor=mydb.cursor()
mycursor.execute("create table sale (s_no varchar(100),month varchar(100),sales varchar(100),stock varchar(100),taxes varchar(100))")
mydb.commit()
print("Table created")
