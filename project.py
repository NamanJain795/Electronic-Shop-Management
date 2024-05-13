print('-----------------------------     ELECTRONICSHOP     ------------------------')
print('\n')

x='y'
while x=='y':
    print('1. Item details')
    print('2. Sale details')
    print('3. Customer details')
    print('4. Labour details')
    print('5. Expenses details')
    print('6. Exit')
    print('\n')
    a=int(input('enter your choice:'))
    print('\n')
    if a==1:
        def id():
            c='y'
            while c=='y':
                print("1. add item details")
                print('2. update item details')
                print('3. display item details')
                print('4. search item details')
                print('5. delete item details')
                print('6. exit item details')
                print('\n')
                q=int(input('enter your choice:'))
                print('\n')
                if q==1:
                    addid()
                elif q==2:
                    upid()
                elif q==3:
                    disid()
                elif q==4:
                    serid()
                elif q==5:
                    delid()
                else:
                    print('returning to main menu')
                    break

        def addid():
            import mysql.connector
            try:
                mydb=mysql.connector.connect(host='localhost',user='root',passwd='',db='electronicshop')
                mycursor=mydb.cursor()
                sno=input('enter sno:')
                itn=input('enter item name:')
                itno=input('enter item no:')
                price=input('enter price:')
                company=input('enter company name:')
                mycursor.execute("""INSERT INTO item(s_no,item_name,item_no,price,company)VALUES(%s,%s,%s,%s,%s)""",(sno,itn,itno,price,company))
                print("Record inserted")
                mydb.commit()
            except Exception as e:
                print("unable to insert record")
                print(e)
        
        def upid():
            import mysql.connector
            try:
                mydb=mysql.connector.connect(host='localhost',user='root',passwd='',db='electronicshop')
                mycursor=mydb.cursor()
                sno=input("enter sno:")
                print("enter new data")
                itn=input("enter item name:")
                itno=input("enter item no:")
                price=input("enter price:")
                company=input("enter company name:")
                mycursor.execute("""update item set item_name=%s,item_no=%s,price=%s,company=%s where s_no=%s""",(itn,itno,price,company,sno))
                mydb.commit()
                print("record updated")
                print('/n')
            except Exception as e:
                print(e)
                print("unable to update record")
                print("\n")

        def disid():
            import mysql.connector 
            from tabulate import tabulate
            try:
                mydb=mysql.connector.connect(host='localhost',user='root',passwd='',db='electronicshop')
                mycursor=mydb.cursor()
                mycursor.execute("SELECT * FROM ITEM")
                result = mycursor.fetchall()
                print(tabulate(result,headers=["s_no","item_name","item_no","price","company"],tablefmt="psql"))
            except Exception as e:
                print("unable to display record")
                print(e)

        def serid():
            import mysql.connector
            from tabulate import tabulate
            try:
                mydb=mysql.connector.connect(host='localhost',user='root',passwd='',db='electronicshop')
                mycursor=mydb.cursor()
                sno=input("enter sno to be searched:")
                mycursor.execute("""SELECT*FROM item where s_no=%s""",(sno,))
                result=mycursor.fetchall()
                print(tabulate(result,headers=["s_no","item_name","item_no","price","company"],tablefmt="psql"))
                print("record displayed")
                mydb.commit()
            except Exception as e:
                print("unable to search record")
                print(e)

        def delid():
            import mysql.connector
            try:
                mydb=mysql.connector.connect(host='localhost',user='root',passwd='',db='electronicshop')
                mycursor=mydb.cursor()
                sno=input("enter sno to delete record for :")
                mycursor.execute("""DELETE FROM item WHERE s_no=%s""",(sno,))
                mydb.commit()
                print("record deleted")
                print("\n")
            except Exception as e:
                print(e)
                print('unable to delete record')
                print("\n")
        id()

    if a==2:
        def sd():
                print("1. add sale details")
                print("2. update sale details")
                print("3. display sale details")
                print("4. search sale details")
                print("5. delete sale details")
                print("6. exit sale details")
                print('\n')
                q=int(input('enter your choice:'))
                print('\n')
                if q==1:
                    addsd()
                elif q==2:
                    upsd()
                elif q==3:
                    dissd()
                elif q==4:
                    sersd()
                elif q==5:
                    delsd()
                else:
                    print('returning to main menu')

        def addsd():
            import mysql.connector
            try:
                mydb=mysql.connector.connect(host='localhost',user='root',passwd='',db='electronicshop')
                mycursor=mydb.cursor()
                sno=input('enter sno:')
                mon=input('enter month:')
                sal=input('enter sale amount:')
                sto=input('enter stock remaining:')
                tax=input('enter taxes applied:')
                mycursor.execute("""INSERT INTO sale(s_no,month,sales,stock,taxes)VALUE(%s,%s,%s,%s,%s)""",(sno,mon,sal,sto,tax))
                print('Record inserted')
                mydb.commit()
            except Exception as e:
                print('unable to insert record')
                print(e)

        def upsd():
            import mysql.connector
            try:
                mydb=mysql.connector.connect(host='localhost',user='root',passwd='',db='electronicshop')
                mycursor=mydb.cursor()
                sno=input("enter sno:")
                print("enter new data")
                mon=input("enter month:")
                sal=input("enter sales:")
                sto=input("enter stock:")
                tax=input("enter taxes:")
                mycursor.execute("""update sale set month=%s,sales=%s,stock=%s,taxes=%s where s_no=%s""",(mon,sal,sto,tax,sno))
                mydb.commit()
                print("record updated")
                print('\n')
            except Exception as e:
                print(e)
                print("unable to update record")
                print("\n")

        def dissd():
            import mysql.connector
            from tabulate import tabulate
            try:
                mydb=mysql.connector.connect(host='localhost',user='root',passwd='',db='electronicshop')
                mycursor=mydb.cursor()
                mycursor.execute("SELECT * FROM SALE")
                result = mycursor.fetchall()
                print(tabulate(result,headers=["s_no","month","sales","stock","taxes"],tablefmt="psql"))
            except Exception as e:
                print('unable to display record')
                print(e)

        def sersd():
            import mysql.connector
            try:
                mydb=mysql.connector.connect(host='localhost',user='root',passwd='',db='electronicshop')
                mycursor=mydb.cursor()
                sno=input('enter sno to be searched:')
                mycursor.execute("""SELECT*FROM sale where s_no=%s""",(sno,))
                result=mycursor.fetchall()
                print(tabulate(result,headers=["s_no","month","sales","stock","taxes"],tablefmt="psql"))
                print("record displayed")
                mydb.commit()
            except Exception as e:
                print("unable to search record")
                print(e)

        def delsd():
            import mysql.connector
            try:
                mydb=mysql.connector.connect(host='localhost',user='root',passwd='',db='electronicshop')
                mycursor=mydb.cursor()
                sno=input("enter sno to delete record for:")
                mycursor.execute("""DELETE FROM sale WHERE s_no=%s""",(sno,))
                mydb.commit()
                print("record deleted")
                print("/n")
            except Exception as e:
                print(e)
                print('unable to delete record')
                print("\n")
        sd()

    if a==3:
        def md():
                print("1. add customer details")
                print("2. update customer details")
                print("3. display customer details")
                print("4. search customer details")
                print("5. delete customer details")
                print("6. exit customer details")
                print('\n')
                q=int(input('enter your choice:'))
                print('\n')
                if q==1:
                    addmd()
                elif q==2:
                    upmd()
                elif q==3:
                    dismd()
                elif q==4:
                    sermd()
                elif q==5:
                    delmd()
                else:
                    print('returning to main menu')

        def addmd():
            import mysql.connector
            try:
                mydb=mysql.connector.connect(host='localhost',user='root',passwd='',db='electronicshop')
                mycursor=mydb.cursor()
                sno=input('enter sno:')
                nam=input('enter name:')
                phn=input('enter phone no:')
                dos=input('enter date of sale:')
                itp=input('enter item purchase:')
                mycursor.execute("""INSERT INTO customer(s_no,name,phone_no,date_of_sale,item_purchase)VALUE(%s,%s,%s,%s,%s)""",(sno,nam,phn,dos,itp))
                print('Record inserted')
                mydb.commit()
            except Exception as e:
                print('unable to insert record')
                print(e)

        def upmd():
            import mysql.connector
            try:
                mydb=mysql.connector.connect(host='localhost',user='root',passwd='',db='electronicshop')
                mycursor=mydb.cursor()
                sno=input("enter sno:")
                print("enter new data")
                nam=input("enter name:")
                phn=input("enter phone no:")
                dos=input("enter date of sale:")
                itp=input("enter item purchase:")
                mycursor.execute("""update customer set name=%s,phone_no=%s,date_of_sale=%s,item_purchase=%s where s_no=%s""",(nam,phn,dos,itp,sno))
                mydb.commit()
                print("record updated")
                print('/n')
            except Exception as e:
                print(e)
                print("unable to update record")
                print("\n")

        def dismd():
            import mysql.connector
            from tabulate import tabulate
            try:
                mydb=mysql.connector.connect(host='localhost',user='root',passwd='',db='electronicshop')
                mycursor=mydb.cursor()
                mycursor.execute("SELECT * FROM CUSTOMER")
                result = mycursor.fetchall()
                print(tabulate(result,headers=["s_no","name","phone_no","date_of_sale","item_purchase"],tablefmt="psql"))
            except Exception as e:
                print('unable to display record')
                print(e)

        def sermd():
            import mysql.connector
            try:
                mydb=mysql.connector.connect(host='localhost',user='root',passwd='',db='electronicshop')
                mycursor=mydb.cursor()
                sno=input('enter sno to be searched:')
                mycursor.execute("""SELECT*FROM customer where s_no=%s""",(sno,))
                result=mycursor.fetchall()
                print(tabulate(result,headers=["s_no","name","phone_no","date_of_sale","item_purchase"],tablefmt="psql"))
                print("record displayed")
                mydb.commit()
            except Exception as e:
                print("unable to search record")
                print(e)

        def delmd():
            import mysql.connector
            try:
                mydb=mysql.connector.connect(host='localhost',user='root',passwd='',db='electronicshop')
                mycursor=mydb.cursor()
                sno=input("enter sno to delete record for :")
                mycursor.execute("""DELETE FROM customer WHERE s_no=%s""",(sno,))
                mydb.commit()
                print("record deleted")
                print("\n")
            except Exception as e:
                print(e)
                print('unable to delete record')
                print("\n")
        md()

    if a==4:
        def nd():
                print("1. add labour details")
                print("2. update labour details")
                print("3. display labour details")
                print("4. search labour details")
                print("5. delete labour details")
                print("6. exit labour details")
                print('\n')
                q=int(input('enter your choice:'))
                print('\n')
                if q==1:
                    addnd()
                elif q==2:
                    upnd()
                elif q==3:
                    disnd()
                elif q==4:
                    sernd()
                elif q==5:
                    delnd()
                else:
                    print('returning to main menu')

        def addnd():
            import mysql.connector
            try:
                mydb=mysql.connector.connect(host='localhost',user='root',passwd='',db='electronicshop')
                mycursor=mydb.cursor()
                sno=input('enter sno:')
                nam=input('enter name:')
                phn=input('enter phone no:')
                sal=input('enter salary:')
                spe=input('enter speciality:')
                mycursor.execute("""INSERT INTO labour(s_no,name,phone_no,salary,speciality)VALUE(%s,%s,%s,%s,%s)""",(sno,nam,phn,sal,spe))
                print('Record inserted')
                mydb.commit()
            except Exception as e:
                print('unable to insert record')
                print(e)

        def upnd():
            import mysql.connector
            try:
                mydb=mysql.connector.connect(host='localhost',user='root',passwd='',db='electronicshop')
                mycursor=mydb.cursor()
                sno=input("enter sno:")
                print("enter new data")
                nam=input("enter name:")
                phn=input("enter phone no:")
                sal=input("enter salary:")
                spe=input("enter speciality:")
                mycursor.execute("""update labour set name=%s,phone_no=%s,salary=%s,speciality=%s where s_no=%s""",(nam,phn,sal,spe,sno))
                mydb.commit()
                print("record updated")
                print('\n')
            except Exception as e:
                print(e)
                print("unable to update record")
                print("\n")

        def disnd():
            import mysql.connector
            from tabulate import tabulate
            try:
                mydb=mysql.connector.connect(host='localhost',user='root',passwd='',db='electronicshop')
                mycursor=mydb.cursor()
                mycursor.execute("SELECT * FROM LABOUR")
                result = mycursor.fetchall()
                print(tabulate(result,headers=["s_no","name","phone_no","salary","speciality"],tablefmt="psql"))
            except Exception as e:
                print('unable to display record')
                print(e)

        def sernd():
            import mysql.connector
            try:
                mydb=mysql.connector.connect(host='localhost',user='root',passwd='',db='electronicshop')
                mycursor=mydb.cursor()
                sno=input('enter sno to be searched:')
                mycursor.execute("""SELECT*FROM labour where s_no=%s""",(sno,))
                result=mycursor.fetchall()
                print(tabulate(result,headers=["s_no","name","phone_no","salary","speciality"],tablefmt="psql"))
                print("record displayed")
                mydb.commit()
            except Exception as e:
                print("unable to search record")
                print(e)

        def delnd():
            import mysql.connector
            try:
                mydb=mysql.connector.connect(host='localhost',user='root',passwd='',db='electronicshop')
                mycursor=mydb.cursor()
                sno=input("enter sno to delete record for :")
                mycursor.execute("""DELETE FROM labour WHERE s_no=%s""",(sno,))
                mydb.commit()
                print("record deleted")
                print("\n")
            except Exception as e:
                print(e)
                print('unable to delete record')
                print("\n")
        nd()

    if a==5:
        def od():
                print("1. add expenses details")
                print("2. update expenses details")
                print("3. display expenses details")
                print("4. search expenses details")
                print("5. delete expenses details")
                print("6. exit expenses details")
                print('\n')
                q=int(input('enter your choice:'))
                print('\n')
                if q==1:
                    addod()
                elif q==2:
                    upod()
                elif q==3:
                    disod()
                elif q==4:
                    serod()
                elif q==5:
                    delod()
                else:
                    print('returning to main menu')

        def addod():
            import mysql.connector
            try:
                mydb=mysql.connector.connect(host='localhost',user='root',passwd='',db='electronicshop')
                mycursor=mydb.cursor()
                sno=input('enter sno:')
                mon=input('enter month:')
                exp=input('enter expenses:')
                amn=input('enter amount:')
                tax=input('enter including taxes:')
                mycursor.execute("""INSERT INTO expenses(s_no,month,expenses,amount,including_taxes)VALUE(%s,%s,%s,%s,%s)""",(sno,mon,exp,amn,tax))
                print('Record inserted')
                mydb.commit()
            except Exception as e:
                print('unable to insert record')
                print(e)

        def upod():
            import mysql.connector
            try:
                mydb=mysql.connector.connect(host='localhost',user='root',passwd='',db='electronicshop')
                mycursor=mydb.cursor()
                sno=input("enter sno:")
                print("enter new data")
                mon=input("enter month:")
                exp=input("enter expenses:")
                amn=input("enter amount:")
                tax=input("enter including taxes:")
                mycursor.execute("""update expenses set month=%s,expenses=%s,amount=%s,including_tax=%s where s_no=%s""",(mon,exp,amn,tax,sno))
                mydb.commit()
                print("record updated")
                print('\n')
            except Exception as e:
                print(e)
                print("unable to update record")
                print("\n")
        def disod():
            import mysql.connector
            from tabulate import tabulate
            try:
                mydb=mysql.connector.connect(host='localhost',user='root',passwd='',db='electronicshop')
                mycursor=mydb.cursor()
                mycursor.execute("SELECT * FROM EXPENSES")
                result = mycursor.fetchall()
                print(tabulate(result,headers=["s_no","month","expenses","amount","including_tax"],tablefmt="psql"))
            except Exception as e:
                print('unable to display record')
                print(e)

        def serod():
            import mysql.connector
            try:
                mydb=mysql.connector.connect(host='localhost',user='root',passwd='',db='electronicshop')
                mycursor=mydb.cursor()
                sno=input('enter sno to be searched:')
                mycursor.execute("""SELECT*FROM expenses where s_no=%s""",(sno,))
                result=mycursor.fetchall()
                print(tabulate(result,headers=["s_no","month","expenses","amount","including_tax"],tablefmt="psql"))
                print("record displayed")
                mydb.commit()
            except Exception as e:
                print("unable to search record")
                print(e)

        def delod():
            import mysql.connector
            try:
                mydb=mysql.connector.connect(host='localhost',user='root',passwd='',db='electronicshop')
                mycursor=mydb.cursor()
                sno=input("enter sno to delete record for :")
                mycursor.execute("""DELETE FROM expenses WHERE s_no=%s""",(sno,))
                mydb.commit()
                print("record deleted")
                print("\n")
            except Exception as e:
                print(e)
                print('unable to delete record')
                print("\n")
        od()

    if a==6:
        exit()

        
        
        


        
        

        
        
        

        
        
        






               
            
                


                
                

        
        
        
        


      


                   
