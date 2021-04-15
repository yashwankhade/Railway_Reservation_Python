import smtplib

sender = 'yashpat181001@gmail.com'

sendpass = 'xyz'
num ='Hardik!'

message =f"""Hello  {num}"""

server = smtplib.SMTP('smtp.gmail.com', 587)

server.starttls()

server.login(sender,sendpass)

print("Logged in")

address_info = 'hardik.21910521@viit.ac.in'

server.sendmail(sender, address_info, message)

