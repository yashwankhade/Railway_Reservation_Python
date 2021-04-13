import sqlite3
from tkinter import *

#root = Tk()
mydb = sqlite3.connect('trains.db')
c= mydb.cursor()

mydb_pass = sqlite3.connect('Passengers.db')
c1 = mydb_pass.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS trains_info(
            train_num INT Primary key,
            Name Text,
            src Text,
            src_time blob,
            dest text,
            dest_time blob,
            fare INT)
            """)

#c.execute("""Insert into trains_info values
#Pune-Mumbai
#   (12890,'Rajdhani Exp','Pune','14:20','Mumbai','17:00',450),
#   (17614,'Panvel Festival Special','Pune','6:20','Mumbai','9:00',120),
#Mumbai-Pune
#(12891,'Sahyadri Exp','Mumbai','14:20','Pune','17:00',80),
#   """)

#mydb.commit()
#db_info = c.execute("SELECT * FROM trains_info")
#for i in db_info:
#   print(i)

c1.execute("""CREATE TABLE IF NOT EXISTS Passenger_info(
             train_num Int Primary Key,
             Name Text,
             Age Int,
             Gender Text,
             Email Text
           )
            """)
   

