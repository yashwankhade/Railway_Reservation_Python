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
    (07614,'Panvel Festival Special','Pune','6:20','Mumbai','9:00',120)
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
            Label(r, text=i[j]).grid(row=1,column=j)
        k=k+1
            

    #for i in mydb:

            #print(str(i[0])+'\t\t\t'+i[1]+'\t'+i[2]+'\t\t'+i[3]+'\t\t'+i[4]+'\t\t'+i[5]+'\t\t'+str(i[6])+'\t\t')

            # Label(r,text=i[j]).grid(row=1,column=j)
            # Label(r,text=i[j]).grid(row=1, column=j)
            # Label(r,text=i[j]).grid(row=1, column=j)
            # Label(r,text=i[j]).grid(row=1, column=j)
            # Label(r,text=i[j]).grid(row=1, column=j)
            # Label(r,text=i[j]).grid(row=1, column=j)
# class Pune_to_Mum:
#     def __init__(self):
#         self.src='Pune'
#         self.dest='Mumbai'
#
#     def trains(self):
#         sql="Select * from trains_info where src='{}' and dest='{}'".format(self.src,self.dest)
#
#         mydb=c.execute(sql)
#         #print("=============================================================================================")
#         #print("Train No.\t\tTrain Name\t\tSource\t\tSource Time\t\tDestination\t\tDestination Time\t\tFare")
#         #print("=============================================================================================")
#         Label(root,text="Train Number").grid(row=0,column=0)
#         Label(root, text="Train Name").grid(row=0,column=1)
#         Label(root, text="Source").grid(row=0, column=2)
#         Label(root, text="Source Time").grid(row=0, column=3)
#         Label(root, text="Destination").grid(row=0, column=4)
#         Label(root, text="Destination Time").grid(row=0, column=5)
#         Label(root, text="Fare").grid(row=0, column=6)
#         for i in mydb:
#
#             print(str(i[0])+'\t\t\t'+i[1]+'\t'+i[2]+'\t\t'+i[3]+'\t\t'+i[4]+'\t\t'+i[5]+'\t\t'+str(i[6])+'\t\t')
#             Label(root,text=i[0]).grid(row=1,column=0)
#             Label(root,text=i[1]).grid(row=1,column=1)
#             Label(root, text=i[2]).grid(row=1, column=2)
#             Label(root, text=i[3]).grid(row=1, column=3)
#             Label(root, text=i[4]).grid(row=1, column=4)
#             Label(root, text=i[5]).grid(row=1, column=5)
#             Label(root, text=i[6]).grid(row=1, column=6)
# obj=Pune_to_Mum()
# obj.trains()
# root.mainloop()

#trains('Mumbai')