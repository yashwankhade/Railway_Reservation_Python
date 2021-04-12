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


enter_train_details()



