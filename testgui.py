import sqlite3
from tkinter import *
import tkinter
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter import messagebox
import trains

global date1
global src

conn = sqlite3.connect('trains.db')
c = conn.cursor()

conn1 = sqlite3.connect('Passengers.db')
c1 = conn1.cursor()

def enter_train_details():
    root = Tk()
    root.geometry('500x400')

    def check():
        if cmb.get() == cmb1.get():
            messagebox.showinfo(
                "Error", "Source and Destination cannot be same")
        else:
            trains10(cmb.get(), cmb1.get())
        date1 = date.get().split('/')
        #print(date1)
        if int(date1[0]) > 31:
            messagebox.showinfo("", "Invalid date")
        root.destroy()

    # Heading
    Heading = Label(root, text="Railway Reservation System",
                    font=30, fg='pink', bg='green', justify='center')
    Heading.grid(row=0, column=3)

    # Source
    source = Label(root, text='Source')
    source.grid(row=1, column=1)
    # Combobox-Source
    cmb = ttk.Combobox(root, width="10", values=(
        "Pune", "Mumbai", "Delhi", "Chennai"))
    cmb.grid(row=1, column=2)

    # Destination
    dest = Label(root, text='Destination')
    dest.grid(row=2, column=1)
    # Combobox-Dest
    cmb1 = ttk.Combobox(root, width="10", values=(
        "Pune", "Mumbai", "Delhi", "Chennai"))
    cmb1.grid(row=2, column=2)

    # Date
    date_label = Label(root, text="Date")
    date_label.grid(row=3, column=1)
    date = Entry(root)
    date.grid(row=3, column=2)
    # Submit Button
    submit = Button(root, text='Show Trains', command=check)
    submit.grid(row=4, column=1)

    # print(selected_month.get())
    root.mainloop()


def trains10(src, dest):
    sql = "Select * from trains_info where src='{}' and dest='{}'".format(src, dest)
    r = Tk()
    info = c.execute(sql)
    # print("=============================================================================================")
    # print("Train No.\t\tTrain Name\t\tSource\t\tSource Time\t\tDestination\t\tDestination Time\t\tFare")
    # print("=============================================================================================")
    Label(r, text="Train Number").grid(row=0, column=0)
    Label(r, text="Train Name").grid(row=0, column=1)
    Label(r, text="Source").grid(row=0, column=2)
    Label(r, text="Source Time").grid(row=0, column=3)
    Label(r, text="Destination").grid(row=0, column=4)
    Label(r, text="Destination Time").grid(row=0, column=5)
    Label(r, text="Fare").grid(row=0, column=6)
    k = 1
    for i in info:
        for j in range(len(i)):
            Label(r, text=i[j]).grid(row=k, column=j)
        k = k+1

    def goback():
        #print("Return Button clicked")
        r.destroy()
        enter_train_details()

    # Return Back Button
    backBtn = Button(r, text="Back", command=goback)
    backBtn.grid(row=k+1, column=0)


def book_a_ticket():
    def into_pass():
        name=name_entry.get()
        age=age_entry.get()
        gender=cmb.get()
        email=email_entry.get()
        train_num=train_no.get()
         
        sql= '''Insert Into Passenger_info Values('%s',%d,'%s','%s',%d)''' % (name,int(age),gender,email,int(train_num))
        c1 = conn1.execute(sql)
        info = c1.execute('select * from Passenger_info')
        for i in info:
            print(i)
    root1 = Tk()
    root1.geometry('600x400')
    root1.title('Book Ticket')

    # Heading
    Heading = Label(root1, text="Book Ticket",font=30, fg='pink', bg='green', justify='center')
    Heading.grid(row=0, column=3)

    # Store name, age, gender, email address
    name = tk.StringVar()
    age = tk.IntVar()
    gender = tk.StringVar()
    email = tk.StringVar()
    train_no = tk.StringVar()

    # Name
    Label(root1, text='Name :').grid(row=2, column=1)
    name_entry = Entry(root1, textvariable=name)
    name_entry.grid(row=2,column=2)
    name_entry.focus()

    # Age
    Label(root1, text='Age : ').grid(row=4, column=1)
    age_entry = Entry(root1, textvariable=age)
    age_entry.grid(row=4, column=2)
    age_entry.focus()

    # Email
    Label(root1, text='Email : ').grid(row=6, column=1)
    email_entry = Entry(root1, textvariable=email)
    email_entry.grid(row=6, column=2)
    email_entry.focus()

    # Gender
    Label(root1, text='Gender : ').grid(row=8, column=1)
    # Combobox
    cmb = ttk.Combobox(root1, width="10", values=("M", "F", "Other"), textvariable=gender)
    cmb.grid(row=8, column=2)

    # Train No
    Label(root1, text='Train No : ').grid(row=10, column=1)
    train_no_label = Entry(root1, textvariable=train_no)
    train_no_label.grid(row=10, column=2)
    train_no_label.focus()

    #Confirm Ticket Button
    b1=Button(root1,text="Confirm Ticket",command=into_pass)
    b1.grid(row=11,column=1)

    #Cancel  Button
    b2=Button(root1,text="Cancel")
    b2.grid(row=11,column=2)
    root1.mainloop()
    

#enter_train_details()
book_a_ticket()




