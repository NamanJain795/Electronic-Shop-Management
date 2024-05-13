#table3 for labour
import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',passwd='',db='electronicshop')
mycursor=mydb.cursor()
mycursor.execute("create table labour (s_no varchar(100),name varchar(100),phone_no varchar(100),salary varchar(100),speciality varchar(100))")
mydb.commit()
print("Table created")
