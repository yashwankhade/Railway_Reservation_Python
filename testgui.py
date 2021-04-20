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
from tkcalendar import DateEntry

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
            cmb_value = cmb.get()
            cmb1_value = cmb1.get()
            root.destroy()
            trains10(cmb_value, cmb1_value)

    def goHome():
        root.destroy()
        homepage()

   # Heading
    Heading = Label(root, text="Railway Reservation System",
                    font=30, fg='pink', bg='green', justify='center')
    Heading.place(x=60, y=25)

    # Source
    source = Label(root, text='Source')
    source.place(x=90, y=130)
    # Combobox-Source
    cmb = ttk.Combobox(root, width="10", values=(
        "Pune", "Mumbai", "Delhi", "Chennai"))
    cmb.place(x=180,y=130)

    # Destination
    dest = Label(root, text='Destination')
    dest.place(x=90,y=190)
    # Combobox-Dest
    cmb1 = ttk.Combobox(root, width="10", values=(
        "Pune", "Mumbai", "Delhi", "Chennai"))
    cmb1.place(x=180,y=190)

    # Submit Button
    submit = Button(root, text='Show Trains', command=check,bg="mint cream")
    submit.place(x=80,y=300)

    # Home Button
    homebtn = Button(root, text='Home', command = goHome,bg="mint cream")
    homebtn.place(x=270,y=300)

    root.mainloop()






#Displaying trains for selected src, dest
def trains10(src, dest):
    r= Tk()

    r.title("AVAILABLE TRAINS")

    window_width = 755
    window_height = 455

    # get the screen dimension
    screen_width = r.winfo_screenwidth()
    screen_height = r.winfo_screenheight()

    # find the center point
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)

    # set the position of the window to the center of the screen
    r.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    treev = ttk.Treeview(r, selectmode ='browse')
  
    # Calling pack method w.r.to treeview
    treev.pack(side ='left')
  
    # Constructing vertical scrollbar
    # with treeview
    verscrlbar = ttk.Scrollbar(r, 
                           orient ="vertical", 
                           command = treev.yview)
  
    # Calling pack method w.r.to verical 
    # scrollbar
    verscrlbar.pack(side ='right', fill ='x')
  
    # Configuring treeview
    treev.configure(xscrollcommand = verscrlbar.set)
  
    # Defining number of columns
    treev["columns"] = ("1", "2", "3", "4","5","6","7")
  
    # Defining heading
    treev['show'] = 'headings'
  
    # Assigning the width and anchor to  the
    # respective columns
    treev.column("1", width = 90, anchor ='c')
    treev.column("2", width = 120, anchor ='ne')
    treev.column("3", width = 90, anchor ='ne')
    treev.column("4", width = 90, anchor ='ne')
    treev.column("5", width = 90, anchor ='ne')
    treev.column("6", width = 90, anchor ='ne')
    treev.column("7", width = 90, anchor ='ne')
  
    # Assigning the heading names to the 
    # respective columns
    treev.heading("1", text ="Train number")
    treev.heading("2", text ="Name")
    treev.heading("3", text ="Source")
    treev.heading("4", text ="Source Time")
    treev.heading("5", text ="Destination")
    treev.heading("6", text ="Destination Time")
    treev.heading("7", text ="Fare")
    sql = "Select * from trains_info where src='{}' and dest='{}'".format(src, dest)
    result = cursor.execute(sql)
    for i in result:
    	treev.insert("", "end", text="", values=(i[0], i[1], i[2], i[3], i[4],i[5],i[6]))
    #GO back to main window from train details window
    def goback():
        #print("Return Button clicked")
        r.destroy()
        enter_train_details()

    def bookTicket():
        r.destroy()
        book_a_ticket()

    

    # Return Back Button
    backBtn = Button(r, text="Back", command=goback,bg="mint cream")
    backBtn.place(x=200,y=400)

    #Book Button
    bookBtn = Button(r, text="Book", command=bookTicket,bg="mint cream")
    bookBtn.place(x=400,y=400)
    r.mainloop()






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
        def generate_pnr():
            low= 10**(8-1)
            high = (10**8)-1
            return random.randint(low,high)
        name=name_entry.get()
        age=age_entry.get()
        gender=cmb.get()
        email=email_entry.get()
        train_num=train_no_label.get()
        email= email_entry.get()
        date = cal.get_date()
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
            print(date)
            c1 = conn1.cursor()
            pnr = generate_pnr()
            print(pnr)
         
            sql= '''Insert Into Passenger_info Values(%d,'%s',%d,'%s','%s',%d)''' % (pnr,name,int(age),gender,email,int(train_num))
            print(sql)
            c1 = conn1.execute(sql)
            info = c1.execute('select * from Passenger_info')
            mydb.commit()
            p=[]
            for i in info:
                p.append(list(i))
            print(p)
            ticket.ticket_display(pnr,int(train_num),p,email,date)
    root1 = Tk()
    
    root1.title('Book Ticket')

    window_width = 600
    window_height = 400

    # get the screen dimension
    screen_width = root1.winfo_screenwidth()
    screen_height = root1.winfo_screenheight()

    # find the center point
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)

    # set the position of the window to the center of the screen
    root1.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    # Heading
    Heading = Label(root1, text="Book Ticket",font=30, fg='pink', bg='green', justify='center')
    Heading.place(x=235, y=10)

    # Store name, age, gender, email address
    name = tk.StringVar()
    age = tk.StringVar()
    gender = tk.StringVar()
    email = tk.StringVar()
    train_no = tk.StringVar()

    # Name
    Label(root1, text='Name :').place(x=180, y=60)
    name_entry = Entry(root1, textvariable=name)
    name_entry.place(x=270,y=60)
    name_entry.focus()

    # Age
    Label(root1, text='Age : ').place(x=180, y=100)
    age_entry = Entry(root1, textvariable=age)
    age_entry.place(x=270, y=100)
    age_entry.focus()

    # Email
    Label(root1, text='Email : ').place(x=180, y=140)
    email_entry = Entry(root1, textvariable=email)
    email_entry.place(x=270, y=140)
    email_entry.focus()

    # Gender
    Label(root1, text='Gender : ').place(x=180,y=180)
    # Combobox
    cmb = ttk.Combobox(root1, width="10", values=("M", "F", "Other"), textvariable=gender)
    cmb.place(x=270, y=180)

    #datetime
    Label(root1, text='Choose date').place(x=180, y=220)
 
    cal = DateEntry(root1, width=12, background='darkblue',
                    foreground='white', borderwidth=2)
    cal.place(x=270,y=220) 

    # Train No
    Label(root1, text='Train No : ').place(x=180, y=260)
    train_no_label = Entry(root1, textvariable=train_no)
    train_no_label.place(x=270, y=260)
    train_no_label.focus()

    #Confirm Ticket Button
    b1=Button(root1,text="Confirm Ticket",command=into_pass,bg="mint cream")
    b1.place(x=180,y=330)

    #Cancel  Button
    b2=Button(root1,text="Cancel", command=cancel,bg="mint cream")
    b2.place(x=390,y=330)
    root1.mainloop()
    





# Homepage
def homepage():
    home = Tk()

    home.title("HOME")
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

    bg = PhotoImage( file = "./images/welcomepage1.png")
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

    # Image using Label
    bg = PhotoImage( file = "./images/homepage.png")
    #Show image using label
    label1 = Label( root, image = bg)
    label1.place(x = 0,y = 0, relwidth=1,relheight=1)

    # Heading
    Head = Label(root, text="Login As",
                    font=30, fg='pink', bg='green', justify='center')
    Head.grid(row=0, column=3,padx=150,pady=40)

    # Guest Button
    Guest = Button(root, text='GUEST', command=guest,bg="gold",fg="red4")
    Guest.place(x=170,y=130)

    # Admin Button
    Admin = Button(root, text='ADMIN', command=admin,bg="gold",fg="red4")
    Admin.place(x=166,y=200)

    root.mainloop()










# ADMIN PART

mydb = sqlite3.connect('trains.db')
cursor = mydb.cursor()
# Verify Email and password wala function
def verification():
    root = Tk()
    root.title("VERIFICATON")
    window_width = 300
    window_height = 200

    # get the screen dimension
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # find the center point
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)

    # set the position of the window to the center of the screen
    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    
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
    st = 'select * from Passenger_info'
    a= cursor.execute(st)
    r = Tk()
    r.title("PASSENGERS INFO")
    window_width = 555
    window_height = 455

    # get the screen dimension
    screen_width = r.winfo_screenwidth()
    screen_height = r.winfo_screenheight()

    # find the center point
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)

    # set the position of the window to the center of the screen
    r.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    
    treev = ttk.Treeview(r, selectmode ='browse')
  
    # Calling pack method w.r.to treeview
    treev.pack(side ='left')
  
    # Constructing vertical scrollbar
    # with treeview
    verscrlbar = ttk.Scrollbar(r, 
                           orient ="vertical", 
                           command = treev.yview)
  
    # Calling pack method w.r.to verical 
    # scrollbar
    verscrlbar.pack(side ='right', fill ='x')
  
    # Configuring treeview
    treev.configure(xscrollcommand = verscrlbar.set)
  
    # Defining number of columns
    treev["columns"] = ("1", "2", "3", "4" , "5" ,"6")
  
    # Defining heading
    treev['show'] = 'headings'
  
    # Assigning the width and anchor to  the
    # respective columns
    treev.column("1", width = 90, anchor ='c')
    treev.column("2", width = 90, anchor ='se')
    treev.column("3", width = 90, anchor ='se')
    treev.column("4", width = 90, anchor ='se')
    treev.column("5", width = 90, anchor ='se')
    treev.column("6", width = 90, anchor ='se')
  
    # Assigning the heading names to the 
    # respective columns
    treev.heading("1", text ="Train no.")
    treev.heading("2", text ="Name")
    treev.heading("3", text ="Age")
    treev.heading("4", text ="Gender")
    treev.heading("5", text ="Email")
    treev.heading("6", text ="PNR")
    st1= 'Select distinct count(pnr) from passenger_info'
    b= cursor.execute(st1)
    for i in b:
        num=i
    Label(r, text="Number of Passengers:").place(x=0,y=0)
    Label(r, text=num).place(x=130,y=0)
    a= conn.execute('select * from passenger_info')
    
    result = a.fetchall()
    for i in result:
    	treev.insert("", "end", text="", values=(i[0], i[1], i[2], i[3], i[4],i[5]))

    # Back Button
    def btn_back():
        r.destroy()
        admin_main()

    Button(r, text='BACK', command = btn_back).place(x=250, y=350)
    r.mainloop()
    r.mainloop()







def show_trains():
    st = 'Select * from trains_info'
    a= cursor.execute(st)
    r = Tk()

    r.title("TRAINS")
    window_width = 755
    window_height = 455

    # get the screen dimension
    screen_width = r.winfo_screenwidth()
    screen_height = r.winfo_screenheight()

    # find the center point
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)

    # set the position of the window to the center of the screen
    r.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    
    k = 1
    b = "select count(*) from trains_info"
    m= cursor.execute(b)
    for num in m:
        print(m)

    treev = ttk.Treeview(r, selectmode ='browse')
    
    Label(r, text=f"Number of Trains : {int(str(num[0]))}").place(x=40,y=50)
    
    # Calling pack method w.r.to treeview
    treev.pack(side ='right')
  
    # Constructing vertical scrollbar
    # with treeview
    verscrlbar = ttk.Scrollbar(r, orient ="vertical", command = treev.yview)
  
    # Calling pack method w.r.to verical 
    # scrollbar
    verscrlbar.pack(side ='right', fill ='x')
  
    # Configuring treeview
    treev.configure(xscrollcommand = verscrlbar.set)
  
    # Defining number of columns
    treev["columns"] = ("1", "2", "3","4","5","6","7")
  
    # Defining heading
    treev['show'] = 'headings'
  
    # Assigning the width and anchor to  the
    # respective columns
    treev.column("1", width = 90, anchor ='c')
    treev.column("2", width = 140, anchor ='ne')
    treev.column("3", width = 90, anchor ='ne')
    treev.column("4", width = 90, anchor ='ne')
    treev.column("5", width = 90, anchor ='ne')
    treev.column("6", width = 98, anchor ='ne')
    treev.column("7", width = 90, anchor ='ne')
  
    # Assigning the heading names to the 
    # respective columns
    treev.heading("1", text ="Train no.")
    treev.heading("2", text ="Name")
    treev.heading("3", text ="Source")
    treev.heading("4", text ="Source Time")
    treev.heading("5", text ="Destination")
    treev.heading("6", text ="Destination Time")
    treev.heading("7", text ="Fare")

    a= conn.execute('select * from trains_info')
    
    result = a.fetchall()
    for i in result:
    	treev.insert("", "end", text="", values=(i[0], i[1], i[2], i[3], i[4],i[5],i[6]))
    for i in a:
        for j in range(len(i)):
            Label(r, text=i[j]).grid(row=k, column=j)
        k = k+1

    # Back Button
    def btn_back():
        r.destroy()
        admin_main()

    Button(r, text='BACK', command = btn_back).place(x=400, y=350)
    r.mainloop()
        






def add_trains():
    root = Tk()
    root.title("ADD TRAINS")
    window_width = 500
    window_height = 500

    # get the screen dimension
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # find the center point
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)

    # set the position of the window to the center of the screen
    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

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
        tnum= t_number.get()
        tname= t_name.get()
        tsrc = src.get()
        tsrct= t_srctime.get()
        tdest = dest.get()
        tdestt = t_desttime.get()
        tfare= t_fare.get()
        print("Added")
       
        st= "insert into trains_info values (%d,'%s','%s','%s','%s','%s',%d)" % (int(tnum),tname,tsrc,tsrct,tdest,tdestt,int(tfare))
        print(st)
        cursor.execute(st)
        mydb.commit()
        messagebox.showinfo('Success','Train record added successfully!')
        print(st)

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
    Heading.place(x=180, y=20)

    # Add Train Details
    Label(root, text='Train Number: ').place(x=100, y=80)
    num = Entry(root, textvariable=t_number)
    num.place(x=250, y=80)
    num.focus()

    Label(root, text='Train Name: ').place(x=100, y=120)
    name = Entry(root, textvariable=t_name)
    name.place(x=250, y=120)
    name.focus()

    Label(root, text='Source: ').place(x=100, y=160)
    src = ttk.Combobox(root, width="10", values=(
        "Pune", "Mumbai", "Delhi", "Chennai"))
    src.place(x=250, y=160)

    Label(root, text='Destination: ').place(x=100, y=200)
    dest = ttk.Combobox(root, width="10", values=(
        "Pune", "Mumbai", "Delhi", "Chennai"))
    dest.place(x=250, y=200)
    
    Label(root, text='Source Time: ').place(x=100, y=240)
    stime = Entry(root, textvariable=t_srctime)
    stime.place(x=250, y=240)
    stime.focus()

    Label(root, text='Destination Time: ').place(x=100,y=280)
    dtime = Entry(root, textvariable=t_desttime)
    dtime.place(x=250, y=280)
    dtime.focus()

    Label(root, text='Fare: ').place(x=100, y=320)
    fare = Entry(root, textvariable=t_fare)
    fare.place(x=250, y=320)
    fare.focus()

    # Add Train Button
    btnAdd = Button(root, text='Add Train', command=add_train)
    btnAdd.place(x=120,y=380)

    # Cancel Button
    btnCancel = Button(root, text='BACK', command=cancel)
    btnCancel.place(x=230,y=380)
    
    # Reset Button
    btnReset = Button(root, text='Reset', command=reset)
    btnReset.place(x=320,y=380)

    root.mainloop()



    



def cancel_trains():
    def cancel():
        tno1 = tnum.get()
        print(tno1)
        #messagebox.showinfo('Success','Train record deleted!')
       
    print('Cancel Trains')
    r = Tk()
    r.title("CANCEL TRAINS")
    tnum = tk.StringVar()
    window_width = 255
    window_height = 255

    # get the screen dimension
    screen_width = r.winfo_screenwidth()
    screen_height = r.winfo_screenheight()

    # find the center point
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)

    # set the position of the window to the center of the screen
    r.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    
    Label(r, text="Enter Train number").pack()
    Entry(r, textvariable=tnum).pack()
    Button(r,text="Cancel", command=cancel).pack()
    
    #st = 'Delete from trains_info where train_num=%d' % int(a.get())
    #cursor.execute(st)
    # mydb.commit()
    
    r.mainloop()
    






def admin_main():
    root = Tk()
    window_width = 300
    window_height = 300

    # get the screen dimension
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # find the center point
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)

    # set the position of the window to the center of the screen
    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    
    root.resizable(True, True)
    root.title('Admin')

    def s_passengers():
        root.destroy()
        show_passengers()

    def s_trains():
        root.destroy()
        show_trains()
    
    def a_trains():
        root.destroy()
        add_trains()

    def c_trains():
        root.destroy()
        cancel_trains()

    def logout():
        root.destroy()
        main_page()
        # We need to make a call to the Login Page
        
    # Making buttons
    btn1 = Button(root, text='Show Passengers', command=s_passengers)
    btn1.place(x=200, y=10)
    btn2 = Button(root, text='Show Trains', command=s_trains)
    btn2.place(x=120, y=40)
    btn3 = Button(root, text='Add Trains', command=a_trains)
    btn3.place(x=110, y=70)
    btn4 = Button(root, text='Cancel Trains', command=c_trains)
    btn4.place(x=110, y=100)
    btn5 = Button(root, text='Logout', command=logout)
    btn5.place(x=120, y=130)

    for widget in root.winfo_children():
        widget.grid(padx=0, pady=3)
    root.mainloop()

main_page()





