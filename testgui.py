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

conn = sqlite3.connect('trains.db')
c = conn.cursor()

conn1 = sqlite3.connect('Passengers.db')
c1 = conn1.cursor()

#Main window enter src,dest
def enter_train_details():
    root = Tk()
    root.title("TRAIN DETAILS")
    traindetail_width = 400
    traindetail_height = 400

    # get the screen dimension
    screen2_width = root.winfo_screenwidth()
    screen2_height = root.winfo_screenheight()

    # find the center point
    center2_x = int(screen2_width/2 - traindetail_width / 2)
    center2_y = int(screen2_height/2 - traindetail_height / 2)

    # set the position of the window to the center of the screen
    root.geometry(f'{traindetail_width}x{traindetail_height}+{center2_x}+{center2_y}')

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
    Heading.place(x=58, y=25)

    # Source
    source = Label(root, text='Source')
    source.place(x=90, y=110)
    # Combobox-Source
    cmb = ttk.Combobox(root, width="10", values=(
        "Pune", "Mumbai", "Delhi", "Chennai"))
    cmb.place(x=180,y=110)

    # Destination
    dest = Label(root, text='Destination')
    dest.place(x=90,y=170)
    # Combobox-Dest
    cmb1 = ttk.Combobox(root, width="10", values=(
        "Pune", "Mumbai", "Delhi", "Chennai"))
    cmb1.place(x=180,y=170)

    # Date
    date_label = Label(root, text="Date")
    date_label.place(x=90,y=230)
    date = Entry(root)
    date.place(x=180, y=230)

    # Submit Button
    submit = Button(root, text='Show Trains', command=check)
    submit.place(x=80,y=300)

    # Home Button
    homebtn = Button(root, text='Home', command = goHome)
    homebtn.place(x=270,y=300)

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
            p=[]
            for i in info:
                p.append(i)
            print(p)
            ticket.ticket_display(pnr,int(train_num),p)
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
    window_width = 400
    window_height = 400

    # get the screen dimension
    screen_width = home.winfo_screenwidth()
    screen_height = home.winfo_screenheight()

    # find the center point
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)

    # set the position of the window to the center of the screen
    home.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

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
        main_page()
        
    bg = PhotoImage( file = "C:\\Users\\hp\\Desktop\\homepage.png")
    #Show image using label
    label1 = Label( home, image = bg)
    label1.place(x = 0,y = 0, relwidth=1,relheight=1)
        
    # Welcome Message and Styling To Do
    Heading = Label(home, text="Welcome to ABC Railways",
                    font=30, fg='misty rose', bg='green4', justify='center')
    Heading.grid(row=0, column=0,padx=70,pady=40)

    # Show Trains
    show_trains = Button(home, text='Show Trains', command=showTrains, bg='gold', fg="red4")
    show_trains.grid(row=3, column=0,pady=15)
  
    # Book a Ticket
    book_ticket = Button(home, text='Book Ticket', command=bookTicket, bg="gold", fg="red4")
    book_ticket.grid(row=5, column=0,pady=15)

    # Exit
    exit_btn = Button(home, text='Exit', command=exitBtn, width=9, bg="gold", fg="red4")
    exit_btn.grid(row=7, column=0,pady=15)

    home.mainloop()







# MAIN PAGE

def main_page():
    root = Tk()
    root.title('LOGIN')

    login_width = 400
    login_height = 400

    # get the screen dimension
    screen1_width = root.winfo_screenwidth()
    screen1_height = root.winfo_screenheight()

    # find the center point
    center1_x = int(screen1_width/2 - login_width / 2)
    center1_y = int(screen1_height/2 - login_height / 2)

    # set the position of the window to the center of the screen
    root.geometry(f'{login_width}x{login_height}+{center1_x}+{center1_y}')

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
    Head.grid(row=0, column=3,padx=150,pady=40)

    # Guest Button
    Guest = Button(root, text='Guest', command=guest)
    Guest.place(x=170,y=130)

    # Admin Button
    Admin = Button(root, text='Admin', command=admin)
    Admin.place(x=166,y=200)

    root.mainloop()








# ADMIN PART

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

    def back_clicked():
        root.destroy()
        main_page()

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

    # Back Button
    back_button = ttk.Button(signin, text="Back", command=back_clicked)
    back_button.pack(fill='x', expand=True, pady=10)

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
        main_page()
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






