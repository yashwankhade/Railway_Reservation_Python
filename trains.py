import sqlite3
from tkinter import *

#root = Tk()
mydb = sqlite3.connect('trains.db')

c= mydb.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS trains_info(
            train_num INT Primary key,
            Name Text,
            src Text,
            src_time blob,
            dest text,
            dest_time blob,
            fare INT)
            """)

c.execute("""Insert into trains_info values
    (12890,'Rajdhani Exp','Pune','14:20','Mumbai','17:00',450),
    (12891,'Sahyadri Exp','Mumbai','14:20','Pune','17:00',80),
    (17614,'Panvel Festival Special','Pune','6:20','Mumbai','9:00',120)

    """)


def trains(src,dest):
    sql = "Select * from trains_info where src='{}' and dest='{}'".format(src,dest)
    r=Tk()
    mydb= c.execute(sql)
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
    k=1
    for i in mydb:
        for j in range(len(i)):
            Label(r, text=i[j]).grid(row=k,column=j)
        k=k+1
            

   