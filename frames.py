from tkinter import *
import sqlite3
import trains

mydb = sqlite3.connect('trains.db')
conn = mydb.cursor()

root = Tk()
def hello1():
    a= conn.execute('select * from trains_info')
    k=n=0
    for i in a:
        Label(frame2, text=i).pack()
        
        k=k+1

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



 