from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter import messagebox
import trains
import sqlite3
import testgui

def main_page():
    root = Tk()
    root.geometry('300x200')
    root.title('Home')

    # Button functions
    def guest():
        root.destroy()
        homepage()
    
    def admin():
        root.destroy()
        verification()

    # Heading
    Head = Label(root, text="Login As",
                    font=30, fg='pink', bg='green', justify='center')
    Head.grid(row=0, column=3)

    # Guest Button
    Guest = Button(root, text='Guest', command=guest)
    Guest.grid(row=1, column=1)

    # Admin Button
    Admin = Button(root, text='Admin', command=admin)
    Admin.grid(row=2, column=1)

    root.mainloop()

mydb = sqlite3.connect('trains.db')
cursor = mydb.cursor()
# Verify Email and password wala function
def verification():
    root = Tk()
    root.geometry('300x200')
    root.resizable(False, False)
    root.title('Sign In')

    # store email address and password
    user = tk.StringVar()
    passw = tk.StringVar()

    def login_clicked():

        if (username.get()=='Admin' or username.get()=='admin' and password.get()=='abc123'):
            root.destroy()
            admin_main()
        else:
            username.delete(0, 'end')
            password.delete(0, 'end')
            messagebox.showinfo("Error", "Incorrect Username or Password")

    # Sign in frame
    signin = ttk.Frame(root)
    signin.pack(padx=10, pady=10, fill='x', expand=True)

    # Username
    username_label = ttk.Label(signin, text="Username:")
    username_label.pack(fill='x', expand=True)

    username = ttk.Entry(signin, textvariable=user)
    username.pack(fill='x', expand=True)
    username.focus()

    # password
    password_label = ttk.Label(signin, text="Password:")
    password_label.pack(fill='x', expand=True)

    password = ttk.Entry(signin, textvariable=passw, show="*")
    password.pack(fill='x', expand=True)

    # login button
    login_button = ttk.Button(signin, text="Login", command=login_clicked)
    login_button.pack(fill='x', expand=True, pady=10)

    root.mainloop()




def show_passengers():
    print('Show Passengers')

def show_trains():
    st = 'Select * from trains_info'
    a= cursor.execute(st)
    r = Tk()
    r.geometry('455x455')
    k = 1
    for i in a:
        for j in range(len(i)):
            Label(r, text=i[j]).grid(row=k, column=j)
        k = k+1
    r.mainloop()
        
        

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

    def reset():
        num.delete(0, 'end')
        name.delete(0, 'end')
        src.delete(0, 'end')
        dest.delete(0, 'end')
        stime.delete(0, 'end')
        dtime.delete(0, 'end')

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
    btnAdd.grid(row=10, column=0, padx=7, pady=20)

    # Cancel Button
    btnCancel = Button(root, text='Cancel', command=cancel)
    btnCancel.grid(row=10, column=1, padx=7, pady=20)
    
    # Reset Button
    btnReset = Button(root, text='Reset', command=reset)
    btnReset.grid(row=10, column=2, padx=7, pady=20)

    root.mainloop()

def cancel_trains():
    print('Cancel Trains')



def admin_main():
    root = Tk()
    root.geometry('250x200')
    root.resizable(True, True)
    root.title('Admin')

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

main_page()