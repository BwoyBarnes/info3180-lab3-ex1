import smtplib

from_name = 'John Brown'
from_addr = 'fakeemail@gmail.com'
to_name  = 'Jim Brown'
to_addr = 'anotherfakeemail@outlook.com'
subject = 'Test Mail 2 - Outlook'
msg = "If you're reading this, then it worked as well again!"

message = """From: {} <{}>
To: {} <{}> 
Subject: {}
{}
"""

message_to_send = message.format(from_name, from_addr, to_name,
 to_addr, subject, msg)

# Credentials (if needed)
username = 'fakeemail@gmail.com'
password = 'insertapppassword'

# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username, password)
server.sendmail(from_addr, to_addr, message_to_send)
server.quit() 