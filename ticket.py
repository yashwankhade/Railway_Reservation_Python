import sqlite3
from sqlite3.dbapi2 import Cursor
from tkinter import *

mydb = sqlite3.connect('trains.db')
cursor = mydb.cursor()


def ticket_display(pnr,trainno):
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

# ========Passenger_info========
    Label(root, text="Passenger Information", font=30).place(x=130, y=150)

    name = Label(root, text="Name").place(x=30, y=200)
    age = Label(root, text="Age").place(x=90, y=200)
    gender = Label(root, text="Gender").place(x=150, y=200)
    pnr = Label(root, text="PNR number").place(x=210, y=200)
    status = Label(root, text="Status").place(x=300, y=200)

    root.mainloop()
