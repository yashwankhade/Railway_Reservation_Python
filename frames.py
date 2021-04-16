from tkinter import *

root = Tk()
def hello1():
    msg=Label(frame2, text="hello")
    msg.pack()
root.geometry('655x355')

frame1=Frame(root, width=100,height=100, highlightbackground='red', highlightthickness=3)
frame1.place(x=20,y=40)
frame2=Frame(root, width=100,height=100, highlightbackground='red', highlightthickness=3)
frame2.place(x=400,y=80)

username = Label(frame1, text="Username")
username.place(x=0,y=0)
button12 = Button(frame1, text="Click me", command=hello1)
button12.place(x=10,y=30)


root.mainloop()



 