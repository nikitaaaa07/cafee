from tkinter import*
import tkinter as tk
import random
import math
import mysql.connector as sqltor
mycon=sqltor.connect(host="localhost",user="root",passwd="1234")#Google@123
if mycon.is_connected()==False:
    print("Error connecting to database")
else:
    print('successfully connected')

cursor=mycon.cursor()


root = tk.Tk()
img=PhotoImage(file='C:\\Users\\Myself\\Documents\\WTPROJECTS\\cafee\\cafe_shop.png')
Label(root,image=img).pack()
tk.Button(root,text="Welcome to cafe",command=root.destroy,bg='light blue').pack()
T = tk.Text(root, height=500, width=300,bg='orange')
T.pack()
T.insert(tk.END, " MENU\nHomemade Cookies\nCheese Balls\nOrganic Crackers\nFruit rollups\nCheeseSpinach roll\nPotato Wedges\nBelgian Chocolate\nTropical Freshner\nCrunchy Butterscoth\nCaramel Mocha\nCoffee\nCola")

root.config(bg='yellow')
tk.mainloop()




#global variables
choice=0
bill=0
def sql():
    

    cursor.execute("Use mysql;")
    
    cursor.execute("Drop table if exists MENU;")
    cursor.execute("CREATE TABLE MENU(Product_ID INT,Product_name VARCHAR(25),Price INT NOT NULL,Inventory INT,Sold INT)")
    cursor.execute("insert into MENU values(%s, '%s', %s, %s, %s)"%(1,'Homemade Cookies',40,50,2))
    cursor.execute("insert into MENU values(%s, '%s', %s, %s, %s)"%(2,'Cheese Balls',55,70,60))
    cursor.execute("insert into MENU values(%s, '%s', %s, %s, %s)"%(3,'Organic Crackers',35,50,40))
    cursor.execute("insert into MENU values(%s, '%s', %s, %s, %s)"%(4,'Fruit rollups',25,35,22))
    cursor.execute("insert into MENU values(%s, '%s', %s, %s, %s)"%(5,'CheeseSpinach roll',45,15,7))
    cursor.execute("insert into MENU values(%s, '%s', %s, %s, %s)"%(6,'Potato Wedges',45,35,19))
    cursor.execute("insert into MENU values(%s, '%s', %s, %s, %s)"%(7,'Belgian Chocolate',40,10,9))
    cursor.execute("insert into MENU values(%s, '%s', %s, %s, %s)"%(8,'Tropical Freshner',55,15,12))
    cursor.execute("insert into MENU values(%s, '%s', %s, %s, %s)"%(9,'Crunchy Butterscoth',55,10,7))
    cursor.execute("insert into MENU values(%s, '%s', %s, %s, %s)"%(10,'Caramel Mocha',45,15,11))
    cursor.execute("insert into MENU values(%s, '%s', %s, %s, %s)"%(11,'Coffee',25,20,16))
    cursor.execute("insert into MENU values(%s, '%s', %s, %s, %s)"%(12,'Cola',30,30,23));
    #add more items to this, Just copy the above execute statement and change values in the bracket after % sign

def sql2():
    
    cursor.execute("Use mysql;")
    cursor.execute("Drop table if exists customers;")
    cursor.execute('CREATE TABLE customers (Id int(3) unique,Name varchar(30) not null,Mobile_no bigint(10) primary key,Email varchar(50),Points bigint(10))')
    cursor.execute("insert into customers values(%s, '%s', %s, '%s', %s)"%(313,'Jacob Wilson',8296683438,'jabonalive@hotmail.com',12))
    cursor.execute("insert into customers values(%s, '%s', %s, '%s', %s)"%(623,'Lara Lopez ',9840154090,'littlelara@yahoo.com',43))
    cursor.execute("insert into customers values(%s, '%s', %s, '%s', %s)"%(578,'Noah',9606344442,'noahmiller@gmail.com',79))
    cursor.execute("insert into customers values(%s, '%s', %s, '%s', %s)"%(902,'Christopher',9502285457,'lucifer1010@outlook.com',98))
    cursor.execute("insert into customers values(%s, '%s', %s, '%s', %s)"%(218,'Hailey Brown',9500037295,'haileybrown@outlook.com',28))
    cursor.execute("insert into customers values(%s, '%s', %s, '%s', %s)"%(423,'Aiden',9970747162,'aiden_79@gmail.com',57));
    
    
def display():
    cursor.execute("select Product_ID,Product_name,Price from MENU")
    data=cursor.fetchall()
    count=0
    for row in data:
        for items in row:
            print(items,end=" ")
        count+=1
        print()
    print("for admin functions enter 123")
    print("0 for exit")
    choices()
def choices():
    global choice
    print("enter product id of the item you want to buy")
    choice=int(input("ID-"))
    if choice==123:
        adlogin()
    elif choice==0:
        print("thank you for visiting  our cafe")
        return 1
    else:
        billing()
def billing():
    global choice
    global bill
    c=choice
    cursor.execute("select Price from MENU where Product_ID = %s"%(c,))
    price=cursor.fetchall()
    #price for the product he selected
    bill+=price[0][0]
    cursor.execute("update MENU set Inventory=Inventory-%s where Product_ID =%s"%(1,choice))
    mycon.commit()
    cursor.execute("update MENU set Sold=Sold+%s where Product_ID =%s"%(1,choice))
    mycon.commit()
    ans=input("do you want to add another item ?")
    if ans=='y':
        choices()
    else:
        print("the total amount to be paid : ",bill)
        points()
        balance()


def checkpoints(num):
    
    try:
       cursor.execute('select Points from customers where Mobile_no=%s'%(num,))
       data=cursor.fetchall()
       point=data[0][0]
       mycon.commit()
       disc(point,num)
    except:
        print("wrong phone number")
        points()
    
        

def points():
    print('do you have memebership?')
    ans=input('n/y')
    if ans=='n':
        
        print('do u want memebership')
        ans=input('n/y')
        if ans=='n':
            print('proceeding to billing')
            
        elif ans=='y':
            new_member()
        
    elif ans=='y':
        print('enter your mobile no')
        num=int(input('mob.no-'))
        checkpoints(num)
    
        

  
  

def disc(points,num):
  global bill
  if points>20 and points<=50:
     bill=bill-.30*bill
     print('proceeding to billing',bill)
     point_red(points,num)
  elif points>50 and points<=100:
     bill=bill-.50*bill
     print('proceeding to billing',bill)
     
     point_red(points,num)
    
  elif points>100:
     bill=bill-.75*bill
     print('proceeding to billing',bill)
     
     point_red(points-100,num)
  else:
     print('no discount')
  point_con()
     
    
def new_member():
  
    name=input('enter your name-')
    email=input('enter your email id-')
    phno=int(input('enter your phone no-'))
    ID=random.randrange(500)
    cursor.execute("insert into customers values(%s,'%s',%s,'%s',%s)"%(ID,name,phno,email,0))
    mycon.commit()
    print('congrats your a new member of our cafe now!!')


def point_con():
    
    point=bill//10
    cursor.execute('update customers set points=points+%s' % (point,))
    print('points added')
    mycon.commit()
def point_red(point,num):
    cursor.execute('update customers set points=points-%s where Mobile_no=%s' % (point,num))
    mycon.commit()
                          
def Insuffcient_balance(amt_due):
    global balance
    print("the amount you paid is insuffcient , amount due : ",amt_due)
    ans=input("do you want to cancel your order")
    if ans=='n':
        paid=int(input("enter the amount paid"))
        balance=paid-amt_due
        if (paid>=amt_due):
            print("amount given back : ",balance)
        else:
            Insuffcient_balance(math.fabs(balance))
    else:
        print("cancelling order")

def balance():
    global bill
    paid=int(input("enter amount paid"))
    balance=paid-bill
    if(paid>=bill):
        print("balance given back : ",balance)
            
        bill=0
        display()
    else:     
        Insuffcient_balance(math.fabs(balance))

def ad():
    
    admin=False
    adchoice=0

def adlogin():
    
    global admin
    global adchoice
           
    user=input("enter username")
    passwrd=input("enter password")
    if user=='admin' and passwrd=='eastblr':
        admin=True
    else:
        admin=False
    if admin:
        admenu()
    else:
        print("wrong username or password")
        display()

def adchoices():
       global adchoice
       print("enter the option you want to use")
       adchoice=int(input(""))
       if adchoice==1:
            showInvent()
            admenu()
       elif adchoice==2:
            showSave()
            admenu()
       elif adchoice==3:
            add()
            admenu()
       elif adchoice==4:
            sub()
            admenu()
       elif adchoice==5:
            changePrice()
            admenu()
       elif adchoice==6:
            changeInventory()
            admenu()
       else:
            display()

 

def admenu():
        global admenu
        global  admin
        print("1.show inventory")
        print("2.show savings")
        print("3.add items")
        print("4.delete items")
        print("5.change prices")
        print("6.change inventory")
        print("7.exit admin")
        adchoices()
   





def showInvent():
    
    cursor.execute("select Product_ID,Product_Name,Inventory from MENU")
    invt=cursor.fetchall()
    for row in invt:
        for items in row:
            print(items,end=" ")
        print()
   
def showSave():
    cursor.execute("select sum(Sold*Price) from MENU")
    saving=cursor.fetchall()
    print("total savings are : ",int(saving[0][0]))
   
def add():
    pid=int(input("enter product id of item"))
    name=input("enter product name")
    price=int(input("enter product price"))
    stock=int(input("enter the no.of items"))
    cursor.execute("insert into MENU values(%s,'%s',%s,%s,%s)"%(pid,name,price,stock,0))
    mycon.commit()
    print("added successfully")
    
def sub():
    pid=int(input("enter the product id for the item to be deleted"))
    cursor.execute("delete from MENU where Product_ID=%s"%(pid,))
    mycon.commit()
    print("deleted successfully")
    
def changePrice():
    pid=int(input("enter the product id for the item's price to be changed"))
    newprice=int(input("enter the new price for the selected item"))
    cursor.execute("update MENU set Price = %s where Product_ID =%s"%(newprice,pid))
    mycon.commit()
    
def changeInventory():
    pid=int(input("enter the product id for the item's stock to be changed"))
    newstock=int(input("enter the new stock"))
    cursor.execute("update MENU set Inventory=%s where Product_ID=%s"%(newstock,pid))
    mycon.commit()



sql()
sql2()
display()
