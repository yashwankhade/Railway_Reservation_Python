import sqlite3
import random
from tkinter import *
import tkinter
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter import messagebox
import trains
import ticket
global date1
global src

conn = sqlite3.connect('trains.db')
c = conn.cursor()

conn1 = sqlite3.connect('Passengers.db')
c1 = conn1.cursor()

#Main window enter src,dest
def enter_train_details():
    root = Tk()
    root.geometry('500x400')

    #Checking values entered
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

    def goHome():
        root.destroy()
        homepage()

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

    # Home Button
    homebtn = Button(root, text='Home', command = goHome)
    homebtn.grid(row=4, column=2)

    root.mainloop()

#Displaying trains for selected src, dest
def trains10(src, dest):
    sql = "Select * from trains_info where src='{}' and dest='{}'".format(src, dest)
    r = Tk()
    info = c.execute(sql)
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
    #GO back to main window from train details window
    def goback():
        #print("Return Button clicked")
        r.destroy()
        enter_train_details()

    # Return Back Button
    backBtn = Button(r, text="Back", command=goback)
    backBtn.grid(row=k+1, column=0)

    #Book Button
    backBtn = Button(r, text="Book", command=book_a_ticket)
    backBtn.grid(row=k+1, column=1)
    
#Passenger Info 
def book_a_ticket():
    
    def ticket_details(pnr):
        st= ' Select * from Passenger_info where train_num=%d' % pnr
        c1=conn1.execute(st)
        for i in c1:
            print(i)


    def cancel():
        root1.destroy()
        
        homepage()
    #Inserting values in Passenger db
    def into_pass():
        def validation(email):
            if '@' not in email:
                return 'Enter valid email!'
        def generate_pnr():
            low= 10**(8-1)
            high = (10**8)-1
            return random.randint(low,high)
        name=name_entry.get()
        age=age_entry.get()
        gender=cmb.get()
        email=email_entry.get()
        train_num=train_no_label.get()
        #messagebox.showinfo('',validation(email))
        if len(name)==0 or  age=='0' or gender=='' or email=='' or train_num=='':
            messagebox.showinfo('Error',"Please fill all details!")
        elif name!='' and age=='' and gender=='' and email=='' and train_num=='':
             messagebox.showinfo('Error',"Please fill all details!")
        elif name!='' and age!='' and gender=='' and email=='' and train_num=='':
             messagebox.showinfo('Error',"Please fill all details!")
        elif name!='' and age!='' and gender!='' and email=='' and train_num=='':
            messagebox.showinfo('Error',"Please fill all details!")
        elif name!='' and age!='' and gender!='' and email!='' and train_num=='':
             messagebox.showinfo('Error',"Please enter train number!") 
        elif '@' not in email:
            messagebox.showinfo('Error',"Please enter valid email id!") 
        elif int(age) not in range(1,100):
            messagebox.showinfo('Error','Enter valid Age!')
        
        else:   
            # name=name_entry.get()
            # age=age_entry.get()
            # gender=cmb.get()
            # email=email_entry.get()
            # train_num=train_no.get()
            c1 = conn1.cursor()
            pnr = generate_pnr()
            print(pnr)
            # p1 = 'Select PNR from Passenger_info'
            # pnr_list = c1.execute(p1)
            # for i in pnr_list:
            #     print(i)
            # if pnr in 
         
            sql= '''Insert Into Passenger_info Values(%d,'%s',%d,'%s','%s',%d)''' % (pnr,name,int(age),gender,email,int(train_num))
            print(sql)
            c1 = conn1.execute(sql)
            info = c1.execute('select * from Passenger_info')
            #conn1.commit()
            #ticket_details(pnr, train_num)
            for i in info:
                print(i)
            ticket.ticket_display(pnr,int(train_num))
    root1 = Tk()
    root1.geometry('600x400')
    root1.title('Book Ticket')

    # Heading
    Heading = Label(root1, text="Book Ticket",font=30, fg='pink', bg='green', justify='center')
    Heading.grid(row=0, column=3)

    # Store name, age, gender, email address
    name = tk.StringVar()
    age = tk.StringVar()
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
    b2=Button(root1,text="Cancel", command=cancel)
    b2.grid(row=11,column=2)
    root1.mainloop()
    

# Homepage
def homepage():
    home = Tk()
    home.geometry('300x300')

    def showTrains():
        #print("Show trains pressed")
        home.destroy()
        enter_train_details()
    
    def bookTicket():
        #print("Book Ticket pressed")
        home.destroy()
        book_a_ticket()

    def exitBtn():
        home.destroy()
        
    # Welcome Message and Styling To Do
    Heading = Label(home, text="Welcome to ABC Railways",
                    font=30, fg='pink', bg='green', justify='center')
    Heading.grid(row=0, column=0)

    # Show Trains
    show_trains = Button(home, text='Show Trains', command=showTrains, bg='yellow', fg="red")
    show_trains.grid(row=3, column=0)
  
    # Book a Ticket
    book_ticket = Button(home, text='Book Ticket', command=bookTicket, bg="yellow", fg="red")
    book_ticket.grid(row=5, column=0)

    # Exit
    exit_btn = Button(home, text='Exit', command=exitBtn, width=9, bg="yellow", fg="red")
    exit_btn.grid(row=7, column=0)

    home.mainloop()

homepage()







