import sqlite3
from sqlite3.dbapi2 import Cursor
from tkinter import *
import smtplib
from tkinter import messagebox
from tkinter.messagebox import showinfo

mydb = sqlite3.connect('trains.db')
cursor = mydb.cursor()



def ticket_display(pnr,trainno,p,email,date):
    #PNR_NUMB=pnr
    em,tn1,p,d=email,trainno,p,date
    def send_email():
        t=[]
        
        st = 'select * from trains_info where train_num=%d' % tn1
        a= cursor.execute(st)
        for i in a:
            print(i)
        sender = '@gmail.com'
        sendpass = ''
        
        num = i[0]
        name = i[1]
        src= i[2]
        srct = i[3]
        dest= i[4]
        destt=i[5]
        fare=i[6]

        message =message = f"""From: ABC Railways <from@fromdomain.com>
To: <{em}>
Subject: Ticket Details

Date: {d}\nTrain no. : {num}\n\nTrain name: {name}\n\nSource: {src}\t\tSource Time: {srct}\n\nDestination: {dest}\nDestination Time: {destt}\n\nFare: {fare}\n\nPassenger Details\n\nPNR: {p[0][0]}\nName: {p[0][1]}\nAge: {p[0][2]}\nGender: {p[0][3]} 
"""
         

        server = smtplib.SMTP('smtp.gmail.com', 587)

        server.starttls()

        server.login(sender,sendpass)

        print("Logged in")

        address_info =  em

        server.sendmail(sender, address_info, message)
        messagebox.showinfo('Status','Email Sent Successfully!')

   # sql = 'select * from passenger_info where pnr=%d' % pnr
    sql1 = 'select * from trains_info where train_num=%d' % trainno
  #  a = cursor.execute(sql)
   # for i in a:
     #   print(i)
    b = cursor.execute(sql1)
    
    for i in b:
        print(i)

    root = Tk()


    root.geometry('455x455')

    root.title('Ticket Details')
# ====================Train Num=============
    train_num = Label(root, text="Train no.:")
    train_num.place(x=30, y=20)

    tn = Label(root, text=i[0])
    tn.place(x=90, y=20)

# =============Train name=================
    train_name = Label(root, text="Train Name")
    train_name.place(x=200, y=20)

    tname = Label(root, text=i[1])
    tname.place(x=290, y=20)

# =========Src============
    src = Label(root, text="Source")
    src.place(x=30, y=60)

    src_name = Label(root, text=i[2])
    src_name.place(x=90, y=60)

# =====Dest======
    dest = Label(root, text="Destination")
    dest.place(x=200, y=60)

    dest_name = Label(root, text=i[4])
    dest_name.place(x=290, y=60)

# ========src_time======
    src_time = Label(root, text="Departure Time :")
    src_time.place(x=30, y=100)

    srct = Label(root, text=i[3])
    srct.place(x=120, y=100)

# ========dest_time======
    dest_time = Label(root, text="Arrival Time :")
    dest_time.place(x=200, y=100)

    dest_t = Label(root, text=i[5])
    dest_t.place(x=290, y=100)

#====date=========

    d1 = Label(root,text="Date").place(x=30,y=130)
    d2 = Label(root, text=d).place(x=70,y=130)

# ========Passenger_info========
    st1 = 'Select * from Passenger_info where pnr=%d' % pnr
    ab=cursor.execute(st1)
    
    Label(root, text="Passenger Information", font=30).place(x=110,y=160)
    pnr= Label(root,text="PNR no.").place(x=30, y=200)
    name= Label(root,text="Name").place(x=120, y=200)
    age= Label(root,text="Age").place(x=250, y=200)
    gender= Label(root,text="Gender").place(x=300, y=200)
    fare = Label (root, text="Fare").place(x=360,y=200)
    email= Button(root, text="Get Email", command=send_email).place(x=170, y=300)


    pnr_no= Label(root,text=p[0][0]).place(x=30,y=220)
    name_= Label(root,text=p[0][1]).place(x=120,y=220)
    age_no= Label(root,text=p[0][2]).place(x=250,y=220)
    gen= Label(root,text=p[0][3]).place(x=300,y=220)
    fare= Label(root,text=i[6]).place(x=360,y=220)
    root.mainloop()
