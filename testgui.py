from tkinter import *
import tkinter
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter import messagebox
import trains

global date1
global src
root = Tk()

root.geometry('500x400')

def check():
    trains.trains(cmb.get())
    date1=date.get().split('/')
    print(date1)
    if int(date1[0])>31:
        messagebox.showinfo("","Invalid date")
    root.destroy()



#Heading
Heading=Label(root, text="Railway Reservation System", font=30, fg='pink', bg='green', justify='center')
Heading.grid(row=0,column=3)

#Source
source = Label(root, text='Source')
source.grid(row=1,column=1)
#Combobox-Source
cmb = ttk.Combobox(root, width="10", values=("Pune","Mumbai","Delhi","Chennai"))
cmb.grid(row=1, column=2)

#Destination
dest = Label(root, text='Destination')
dest.grid(row=2,column=1)
#Combobox-Dest
cmb1 = ttk.Combobox(root, width="10", values=("Pune","Mumbai","Delhi","Chennai"))
cmb1.grid(row=2, column=2)

#Date
date_label=Label(root, text="Date")
date_label.grid(row=3,column=1)
date = Entry(root)
date.grid(row=3,column=2)
#Submit Button
submit= Button(root, text='Show Trains', command=check)
submit.grid(row=4,column=1)


#print(selected_month.get())
root.mainloop()


