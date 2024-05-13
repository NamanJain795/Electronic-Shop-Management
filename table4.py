#table4 for customers
import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',passwd='',db='electronicshop')
mycursor=mydb.cursor()
mycursor.execute("create table customer (s_no varchar(100),name varchar(100),phone_no varchar(100),date_of_sale varchar(100),item_purchase varchar(100))")
mydb.commit()
print("Table created")
