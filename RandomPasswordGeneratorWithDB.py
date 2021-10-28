import random
import pyperclip
from tkinter import *
import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="MySql@123#456",
    database="randompassword"
)
# cur=mydb.cursor()
# cur.execute("CREATE DATABASE randomPassword")

# cur=mydb.cursor()
# s="CREATE TABLE RandomPasswords(S_no int(4), Password varchar(20))"
# cur.execute(s)

root=Tk()
root.title("Random Password generator")
root.geometry("220x280")
root.wm_minsize(width=220, height=280)
root.config(bg='lightgreen')

def GeneratePassword():
    e2.delete(0, END)

    length=int(passwordLength.get())

    lower="abcdefghijklmnopqrstuvwxyz"
    upper="ABCDEFGHIJKLMNOPQRSTUVabcdefghijklmnopqrstuvwxyz"
    digits="ABCDEFGHIJKLMNOPQRSTUVabcdefghijklmnopqrstuvwxyz123456789!@#$%^&*()_+~<>?"
    password=""

    if v.get()==1:
        for i in range(1, length+1):
            password += random.choice(lower)
        e2.insert(0,"   "+password)
    
    elif v.get()==2:
        for i in range(1, length+1):
            password += random.choice(upper)
        e2.insert(0,"   "+password)
    
    else:
        for i in range(1, length+1):
            password += random.choice(digits)
        e2.insert(0,"   "+password)

def copy1():
    cur=mydb.cursor()
    s="SELECT * FROM randompasswords"
    cur.execute(s)
    result=cur.fetchall()
    emptyList=[]
    if result==emptyList:
        j=0
    else:
        ll1=list(result)
        ll2=ll1[-1]
        ll3=list(ll2)
        j=ll3[0]
    copyedPassword = e2.get()
    if(copyedPassword != ""):
        pyperclip.copy(copyedPassword)
        x=pyperclip.paste()
        cur=mydb.cursor()
        s="INSERT INTO RandomPasswords(S_no, Password) VALUES(%s, %s)"
        j+=1
        p1=(j, x)
        cur.execute(s, p1)
        mydb.commit()
        e2.delete(0, END)

l1=Label(root, text="Length of password", bg='lightgreen')
l1.place(x=10, y=10, width=200, height=20)

passwordLength=StringVar()
e1=Entry(root, textvariable=passwordLength)
e1.insert(0, "   5")
e1.place(x=90, y=35, width=30, height=20)

l2=Label(root, text="Strength of password", bg='lightgreen')
l2.place(x=8, y=65, width=200, height=20)

v=IntVar()
v.set(2)
rb1=Radiobutton(root, text='Low', variable=v, value=1, bg='lightgreen')
rb1.place(x=75, y=95, height=20)
rb2=Radiobutton(root, text='Medium', variable=v, value=2, bg='lightgreen')
rb2.place(x=75, y=125, height=20)
rb3=Radiobutton(root, text='High', variable=v, value=3, bg='lightgreen')
rb3.place(x=75, y=155, height=20)

e2=Entry(root)
e2.place(x=67, y=190, width=80, height=20)

b2=Button(root, text="Copy", command=copy1)
b2.place(x=85, y=220)

b1=Button(root, text="Generate Password", command=GeneratePassword)
b1.place(x=50, y=250)

root.mainloop()