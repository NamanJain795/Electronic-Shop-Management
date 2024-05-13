#table1 for item
import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',passwd='',db='electronicshop')
mycursor=mydb.cursor()
mycursor.execute("create table item (s_no varchar(100),item_name varchar(100),item_no varchar(100),price varchar(100),company varchar(100))")
mydb.commit()
print("Table created")
