from tkinter import *
import tkinter as ttk
from tkinter import ttk
import tkinter as tk
import sqlite3
import trains

mydb = sqlite3.connect('trains.db')
conn = mydb.cursor()

root = Tk()
def hello1():
    treev = ttk.Treeview(root, selectmode ='browse')
  
# Calling pack method w.r.to treeview
    treev.pack(side ='right')
  
# Constructing vertical scrollbar
# with treeview
    verscrlbar = ttk.Scrollbar(root, 
                           orient ="vertical", 
                           command = treev.yview)
  
# Calling pack method w.r.to verical 
# scrollbar
    verscrlbar.pack(side ='right', fill ='x')
  
# Configuring treeview
    treev.configure(xscrollcommand = verscrlbar.set)
  
# Defining number of columns
    treev["columns"] = ("1", "2", "3")
  
# Defining heading
    treev['show'] = 'headings'
  
# Assigning the width and anchor to  the
# respective columns
    treev.column("1", width = 90, anchor ='c')
    treev.column("2", width = 90, anchor ='ne')
    treev.column("3", width = 90, anchor ='ne')
  
# Assigning the heading names to the 
# respective columns
    treev.heading("1", text ="Name")
    treev.heading("2", text ="Sex")
    treev.heading("3", text ="Age")

    a= conn.execute('select * from trains_info')
    
    result = a.fetchall()
    for i in result:
    	treev.insert("", "end", text="", values=(i[0], i[1], i[2], i[3], i[4]))
  
    # EmployView=ttk.Treeview(frame2)
    # EmployView['columns']=("firstname","secondname","gender","jobtype","hourlywage")
    # EmployView.grid(row=2,column=1,columnspan=1)
    # EmployView.heading("#0",text="",anchor="w")
    # EmployView.column("#0",anchor="center",width=2)
    # a= conn.execute('select * from trains_info')
    
    # result = a.fetchall()
    # for i in result:
    # 	EmployView.insert("", "end", text="", values=(i[0], i[1], i[2], i[3], i[4]))

    # k=n=0
    # for i in a:
    #     Label(frame2, text=i).pack()
        
    #     k=k+1

def hello23():
    Label(frame2, text='kgifufjk').pack()
    
root.geometry('655x355')

frame1=Frame(root, width=100,height=100, highlightbackground='red', highlightthickness=3)
frame1.place(x=20,y=40)
frame2=Frame(root, width=100,height=100, highlightbackground='red', highlightthickness=3)
frame2.place(x=400,y=80)

username = Label(frame1, text="Username")
username.place(x=0,y=0)
button12 = Button(frame1, text="Click me", command=hello1)
button12.place(x=10,y=30)
button1 = Button(frame1, text="Click me", command=hello23)
button1.place(x=70,y=30)


root.mainloop()



 