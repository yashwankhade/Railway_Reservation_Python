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

#c.execute("""Insert into trains_info values
#    (12890,'Rajdhani Exp','Pune','14:20','Mumbai','17:00',450),
#    (12891,'Sahyadri Exp','Mumbai','14:20','Pune','17:00',80),
#    (17614,'Panvel Festival Special','Pune','6:20','Mumbai','9:00',120)
#    """)

#mydb.commit()
#db_info = c.execute("SELECT * FROM trains_info")
#for i in db_info:
#    print(i)


   