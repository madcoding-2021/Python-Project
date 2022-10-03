from tkinter import *
from PIL import ImageTk,Image
import mysql.connector as mysql
import os
import calendar
    
     
def register_user():
    username_info=username.get()
    password_info=password.get()
    
    #connecton to database
    try:
        global db
        db=mysql.connect(host="localhost",user="root",password="root123")
        print("Connected successfully")
    except Exception as e:
        print(e)
        print("failed to connect")
    global a   
    a=username_info
    #database creation
    try:  
        global command_handler
        command_handler = db.cursor()
        command_handler.execute("CREATE DATABASE "+a)
        print("query ok,database created")
        db.commit()
    except Exception as e:
        print("query failed")
        print(e)
    
    global b
    b="LOGIN"
    #table creation for login
    
    try:
        command_handler.execute("USE "+a)
        command_handler = db.cursor()
        command_handler.execute("CREATE TABLE "+b+" (username VARCHAR(20), password VARCHAR(20))")
        print("table creation successful")
        query="INSERT INTO "+b+"(username,password) VALUES('{}','{}')".format(username_info,password_info)
        command_handler.execute(query)
        db.commit()
        print(command_handler.rowcount,"record inserted")
    except Exception as e:
        print("Tabl creation / insertion is unsuccessful due to...")
        Label(screen1,text="User already exsists,Enter other username/login").pack()
        Button(screen1,text ="Retry",command=retry).pack()
        Button(screen1,text = "Login",command=login12).pack()
        screen1.mainloop()
    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(screen1,text="Registration sucessful",fg="green",font=("Calibri",11)).pack()

def login12():
    login1()
    
def register():
    global screen1
    
    screen1=Toplevel(screen)
    screen1.title("register")
    screen1.geometry("1000x1000")
    
    global username,password,username_entry,password_entry
    
    username = StringVar()
    password= StringVar()
    Label(screen1,text = "please enter the details below:" ).pack()
    Label(screen1,text = "" ).pack()
    Label(screen1,text = "username:" ).pack()
    username_entry=Entry(screen1,textvariable=username)
    username_entry.pack()
    Label(screen1,text = "password:").pack()
    password_entry = Entry(screen1,textvariable=password)
    password_entry.pack()
    Label(screen1,text = "").pack()
    Button(screen1,text="Register",width=10,height=1,command=register_user).pack()

def delete2():
    screen3.destroy()
    
def delete3():
    screen4.destroy()
    
def delete4():
    screen5.destroy()
    
def delete5():
    screen9.destroy()
    
def delete6():
    screen2.destroy()
    
def retry():
    username_entry.delete(0,END)
    password_entry.delete(0,END)
    
def save():
    tk=task.get()
    sdate=stdate.get()
    edate=enddate.get()
    lev=lvl.get()
    comp=compl.get()
    
    try:
        command_handler2=db1.cursor()
        print("s")
        command_handler2.execute("USE "+username1)
        print("s")
        try:
            command_handler2.execute("CREATE TABLE TASKSqwer (taskname VARCHAR(30) ,strdate DATE ,eddate DATE ,level INT(1) ,compln VARCHAR(1))")
            print("s")
        except Exception as e:
            query2="INSERT INTO TASKSqwer(taskname,strdate,eddate,level,compln) VALUES('{}','{}','{}','{}','{}')".format(tk,sdate,edate,lev,comp)
        #need to fix for mutiple tasks enteringf same table "tasks",may be using the try and exception I think so... 
            command_handler2.execute(query2)
            print("insertion completed")
        db1.commit()
        Label(screen9,text="Task creation sucessful",fg="green",font=("Calibri",11)).pack()
        Button(screen9,text ="Ok",command=delete5).pack()
    except Exception as e:
        print("insertion failed due to...")
        print(e)
    
def selftask():
    global task,stdate,enddate,lvl,compl,screen9
    task=StringVar()
    stdate=StringVar()
    enddate=StringVar()
    lvl=StringVar()
    compl=StringVar()
    
    screen9 = Toplevel(screen8)
    screen9.title("TYPE THE TASK(S) BELOW")
    screen9.geometry("1500x1000")
    Label(screen9,text = "Please enter the Task:").pack()
    Entry(screen9,textvariable = task).pack()
    Label(screen9,text="").pack()
    Label(screen9,text="Enter the starting date in date format (yy/mm/dd) :").pack()
    Entry(screen9,textvariable = stdate).pack()
    Label(screen9,text="").pack()
    Label(screen9,text ="Enter the deadline in date format (yy/mm/dd)").pack()
    Entry(screen9,textvariable = enddate).pack()
    Label(screen9,text ="").pack()
    Label(screen9,text ="Enter the importance level(OUT OF 5):").pack()
    Entry(screen9,textvariable = lvl).pack()
    Label(screen9,text ="").pack()
    Label(screen9,text="Completion:[S/N]").pack()
    Entry(screen9,textvariable = compl).pack() #make this a label with test condition
    Button(screen9,text="SAVE",command = save).pack()
    
def showCal(): 
    new_gui=Tk() 
    new_gui.config(background="white") 
    new_gui.title("CALENDER") 
    new_gui.geometry("1000x1000") 
    fetch_year=int(year_field.get()) 
    cal_content=calendar.calendar(fetch_year) 
    cal_year=Label(new_gui,text=cal_content,font="Consolas 10 bold") 
    cal_year.grid(row=5,column=1,padx=20) 
    new_gui.mainloop()
def calc1():
    global year_field
    gui=Tk() 
    gui.config(background="white") 
    gui.title("CALENDER") 
    gui.geometry("250x140") 
    cal=Label(gui,text="CALENDAR",bg="dark gray",font=("times",28,'bold')) 
    year=Label(gui,text="Enter Year",bg="light green") 
    year_field=Entry(gui) 
    Show=Button(gui,text="Show Calendar",fg="Black",bg="Red",command=showCal) 
    cal.grid(row=1,column=1) 
    year.grid(row=2,column=1) 
    year_field.grid(row=3,column=1) 
    Show.grid(row=4,column=1)  
    gui.mainloop()
        
def timetable():
    print("will do")    
    
def login_session():
    global screen8
    screen8=Toplevel(screen)
    screen8.title("dashboard")
    screen8.geometry("1500x1000")
    Label(screen8,text="welcome to dashboard").pack()
    Button(screen8,text = "self deadline",command = selftask).pack()
    Button(screen8,text = "monthly calendar",command=calc1).pack()
    Button(screen8,text = "Draft and download own schedule",command = timetable).pack()

def login_sucess():
    delete6()
    login_session()
    
def password_incorrect():
    global screen4
    screen4=Toplevel(screen)
    screen4.title("INCORRECT PASSWORD")
    screen4.geometry("1500x1000")
    Label(screen4,text="re enter the password").pack()
    Button(screen4,text ="Retry",command=delete3).pack()
    
def user_not_found():
    global screen5
    screen5=Toplevel(screen)
    screen5.title("UNKNOWN USER")
    screen5.geometry("1500x1000")
    Label(screen5,text="User not found").pack()
    Button(screen5,text="Return",command=delete4).pack()

def login_verify():
    global username1,password1
    username1=username_verify.get()
    password1=password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)
    
    ab=()
    global db1
    
    try:
        db1 = mysql.connect(host="localhost",user="root",password="hari12",database=username1)
        command_handler2 = db1.cursor()
        print("Connected to schedule databse successfully")
    except Exception as e:
        print(e)
    
    try:
        command_handler2 = db1.cursor()
        command_handler2.execute("SHOW DATABASES")
        print("The databases available are:")
        for i in command_handler2:
            ab+=i
    except Exception as e:
        print("could not show all databases due to...")
        print(e)
    print(ab)
    
    cde=()
    
    try:
        command_handler2= db1.cursor()
        command_handler2.execute("SELECT username,password FROM LOGIN")
        data = command_handler2.fetchall()
        #print(command_handler2)
        db1.commit()
        for j in data:
            cde+=j
    except Exception as e:
        print("couldnot show all tables...")
        print(e)

    print(cde)
        
    if username1 in ab:
        if username1 in cde and password1 in cde:
            login_sucess()
        elif username1 in cde:
            password_incorrect()
    else:
        user_not_found()
    
def login1():
    global screen2
    global screen
    screen2=Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("3000x2500")
    
    global username_verify,password_verify
    
    username_verify=StringVar()
    password_verify=StringVar()
    
    Label(screen2,text="please enter the details below to login:").pack()
    Label(screen2,text="").pack()
    Label(screen2,text="username:").pack()
    
    global username_entry1,password_entry1
    
    username_entry1=Entry(screen2,textvariable=username_verify)
    username_entry1.pack()
    Label(screen2,text="").pack()
    Label(screen2,text="password:").pack()
    password_entry1=Entry(screen2,textvariable=password_verify)
    password_entry1.pack()
    Label(screen2,text="").pack()
    Button(screen2,text="Login",width=10,height=1,command=login_verify).pack()
  
def mainscreen():
    global screen
    screen=Tk()
    screen.geometry("3000x3000")
    screen.title("Schedule Manager")
    
    login=LabelFrame(screen,text="Welcome to Schedule Manager",font=("Times New Roman",20),width=355,height=200,bg="white")
    login.place(x=550,y=350)
    Button(login,text="Login",font=("Times New Roman",15),command=login1).place(x=140,y=25)
    Button(login,text="Register",font=("Times New Roman",15),command=register).place(x=130,y=75)            
    screen.mainloop()
mainscreen()
