import sqlite3
from tkinter import *

#root = Tk()
mydb = sqlite3.connect('trains.db')
c = mydb.cursor()

#mydb_pass = sqlite3.connect('Passengers.db')
#c1 = mydb_pass.cursor()
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
'''
c.execute("""Insert into trains_info values
          (12124,'Deccan Queen','Pune','07:15','Mumbai','10:25',385),
          (02702,'HYB CSMT SPL','Pune','13:15','Mumbai','16:55',500),
          (02208,'Latur CSMT Special','Pune','04:15','Mumbai','07:55',455),
          
          (02779,'Goa Express','Pune','04:30','Delhi','06:25',2838),
         (02629,'Sampark Kranti','Pune','09:10','Delhi','11:25',2504),
          (07305,'NZM Link Express','Pune','04:30','Delhi','06:05',2100),
          (12493,'Darshan Express','Pune','05:15','Delhi','05:35',3850),
         (12147,'Nizamuddin Express','Pune','04:10','Delhi','05:10',2038),
          
          (12163,'LTT Chennai Express','Pune','12:10','Chennai','19:45',2383),
          (19420,'ADI Chennai Express','Pune','21:15','Chennai','17:10',2132),
          (11017,'LTT Karaikal Express','Pune','15:35','Chennai','11:38',2300),
         (11014,'CSMT Chennai Express','Pune','18:10','Chennai','16:20',1999),
          (06502,'ADI MAS SPL','Pune','21:15','Chennai','17:10',2085),         
          
          (11091,'Bhuj Pune Express','Mumbai','12:10','Pune','04:35',495),
          (11043,'LTT Madurai Express','Mumbai','12:15','Pune','03:50',495),
          (11049,'Kolhapur Express','Mumbai','03:35','Pune','07:40',565),
          (02297,'Pune Duronto','Mumbai','03:50','Pune','07:10',625),         
          
         (19019,'Fehradun Express','Mumbai','02:17','Delhi','05:25',1440),
          (22655,'Tvc Nzm Express','Mumbai','19:25','Delhi','15:55',1490),
         (12471,'Swaraj Express','Mumbai','19:55','Delhi','16:35',1735),
          (12499,'Darshan Express','Mumbai','21:00','Delhi','17:35',1490),
          (02617,'Mangaldweep Express','Mumbai','12:40','Delhi','13:25',1735),        
          
         (12136,'LTT Chennai Exp','Mumbai','20:30','Chennai','19:45',2383),
         (19400,'ADI Chennai Exp','Mumbai','17:15','Chennai','17:10',2132),
         (11077,'LTT Karaikal Exp','Mumbai','12:35','Chennai','11:38',2300),
         (11041,'CSMT Chennai Exp','Mumbai','14:10','Chennai','16:20',1999),
         (06052,'ADI MAS SPL','Mumbai','17:05','Chennai','17:10',2085),          
          
         (11078,'Jhelum Express','Delhi','10:15','Pune','15:15',1450),
          (12782,'Swarna Jayanthi','Delhi','05:50','Pune','09:15',1930),
         (12148,'NZM KOP Express','Delhi','05:50','Pune','09:15',1625),
          (12780,'Goa Express','Delhi','15:00','Pune','16:20',1400),
          (12494,'Darshan Express','Delhi','21:35','Pune','21:25',1395),       
          
          (22222,'CSMT Rajdhani','Delhi','17:15','Mumbai','11:50',2100),
          (12432,'Trivandrum Rajdhani','Delhi','10:55','Mumbai','04:25',1950),
          (12264,'Pune Duranto Express','Delhi','10:55','Mumbai','05:50',2200),
          (12910,'BDTS Garib Rath','Delhi','15:35','Mumbai','08:10',1890),
          (12952,'Mumbai Rajdhani','Delhi','16:25','Mumbai','08:15',1789),
          
          (16032,'Andaman Express','Delhi','14:15','Chennai','10:10',2900),
          (12462,'Thirukkural Express','Delhi','07:10','Chennai','18:53',3850),
          (12616,'Grand Trunk Express','Delhi','18:40','Chennai','06:20',2850),
          (12622,'Tamil Nadu Express','Delhi','22:30','Chennai','07:10',2910),
          (12434,'Chennai Rajdhani','Delhi','15:55','Chennai','20:40',4210),
          
         (11042,'Mumbai Express','Chennai','12:20','Pune','09:30',1700),
          (11018,'KIK LTT Express','Chennai','21:05','Pune','19:50',1789),
          (11074,'Chennai LTT Express','Chennai','15:50','Pune','11:55',2100),
         (22919,'Mas ADI Humsafar','Chennai','20:30','Pune','16:30',1970),
         (12164,'MAS LTT Express','Chennai','06:45','Pune','02:20',1890),
          
         (19042,'Mumbai Express','Chennai','12:20','Mumbai','12:35',1790),
         (19018,'KIK LTT Express','Chennai','21:05','Mumbai','11:45',1689),
         (19074,'Chennai LTT Express','Chennai','15:50','Mumbai','16:00',2150),
         (29919,'Mas ADI Humsafar','Chennai','20:30','Mumbai','21:05',1938),
         (19164,'MAS LTT Express','Chennai','06:45','Mumbai','06:00',1890),
          
         (16031,'Andaman Express','Chennai','05:15','Delhi','11:00',1910),
         (12615,'Grand Trunk Express','Chennai','19:15','Delhi','06:30',2050),
         (12687,'Dehradun Express','Chennai','10:00','Delhi','20:40',1890),
          (12651,'Sampark Kranti','Chennai','08:05','Delhi','18:00',2200),
          (12621,'Tamil Nadu Express','Chennai','22:00','Delhi','07:05',1990)
           
          """)
'''
#mydb.commit()
#db_info = c.execute("SELECT * FROM trains_info")
#for i in db_info:
#   print(i)

c.execute("""CREATE TABLE IF NOT EXISTS Passenger_info(
             train_num Int,
             Name Text,
             Age Int,
             Gender Text,
             Email Text,
             PNR Primary key,
             FOREIGN KEY(train_num)
             References trains_info(train_num)
           )
            """)
   
#a1= c1.execute('drop table passenger_info')
# a1= c1.execute('select * from Passenger_info')
# for i in a1:
#   print(i)