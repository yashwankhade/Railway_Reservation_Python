from tkinter import *
import tkinter as tk
from tkinter import ttk

def show_passengers():
    print('Show Passengers')

def show_trains():
    print('Show Trains')

def add_trains():
    root = Tk()
    root.geometry('600x600')

    # Defining Inputs
    t_number = tk.StringVar()
    t_name = tk.StringVar()
    t_src = tk.StringVar()
    t_dest = tk.StringVar()
    t_srctime = tk.StringVar()
    t_desttime = tk.StringVar()
    t_fare = tk.StringVar()

    # Button functions
    def add_train():
        print("Added")

    def cancel():
        root.destroy()
        admin_main()

    # Heading
    Heading = Label(root, text="Add Trains",
                    font=30, fg='pink', bg='green', justify='center')
    Heading.grid(row=0, column=3)

    # Add Train Details
    Label(root, text='Train Number: ').grid(row=2, column=0)
    num = Entry(root, textvariable=t_number)
    num.grid(row=2, column=1)
    num.focus()

    Label(root, text='Train Name: ').grid(row=3, column=0)
    name = Entry(root, textvariable=t_name)
    name.grid(row=3, column=1)
    name.focus()

    Label(root, text='Source: ').grid(row=4, column=0)
    src = ttk.Combobox(root, width="10", values=(
        "Pune", "Mumbai", "Delhi", "Chennai"))
    src.grid(row=4, column=1)

    Label(root, text='Destination: ').grid(row=5, column=0)
    dest = ttk.Combobox(root, width="10", values=(
        "Pune", "Mumbai", "Delhi", "Chennai"))
    dest.grid(row=5, column=1)
    
    Label(root, text='Source Time: ').grid(row=6, column=0)
    stime = Entry(root, textvariable=t_srctime)
    stime.grid(row=6, column=1)
    stime.focus()

    Label(root, text='Destination Time: ').grid(row=7, column=0)
    dtime = Entry(root, textvariable=t_desttime)
    dtime.grid(row=7, column=1)
    dtime.focus()

    # Add Train Button
    btnAdd = Button(root, text='Add Train', command=add_train)
    btnAdd.grid(row=10, column=0, padx=20, pady=20)

    # Cancel Button
    btnAdd = Button(root, text='Cancel', command=cancel)
    btnAdd.grid(row=10, column=1, padx=20, pady=20)

    # CAN WE ADD A RESET BUTTON HERE ?

    root.mainloop()

def cancel_trains():
    print('Cancel Trains')



def admin_main():
    root = Tk()
    root.geometry('200x200')
    root.resizable(True, True)

    def s_passengers():
        #root.destroy()
        show_passengers()

    def s_trains():
        #root.destroy()
        show_trains()
    
    def a_trains():
        root.destroy()
        add_trains()

    def c_trains():
        #root.destroy()
        cancel_trains()

    def logout():
        root.destroy()
        # We need to make a call to the Login Page
        
    # Making buttons
    btn1 = Button(root, text='Show Passengers', command=s_passengers)
    btn1.grid(row=0, column=0)
    btn2 = Button(root, text='Show Trains', command=s_trains)
    btn2.grid(row=1, column=0)
    btn3 = Button(root, text='Add Trains', command=a_trains)
    btn3.grid(row=2, column=0)
    btn4 = Button(root, text='Cancel Trains', command=c_trains)
    btn4.grid(row=3, column=0)
    btn5 = Button(root, text='Logout', command=logout)
    btn5.grid(row=4, column=0)

    for widget in root.winfo_children():
        widget.grid(padx=0, pady=3)
    root.mainloop()

admin_main()