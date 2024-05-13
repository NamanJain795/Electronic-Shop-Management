#table5 for expenses
import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',passwd='',db='electronicshop')
mycursor=mydb.cursor()
mycursor.execute("create table expenses (s_no varchar(100),month varchar(100),expenses varchar(100),amount varchar(100),including_taxes varchar(100))")
mydb.commit()
print("Table created")
