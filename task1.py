
# This is basically a module which provide a client session object which can be used to send mail to receiver
import smtplib
# THis ia type of email object which allows us to send email with different possible attributes
from email.mime.multipart import MIMEMultipart

# Defining sender email and password
sender = ""
password = ""

#  receivers list which can allow us to send email to multiple account at time
receivers = [""]

# Taking subject, body and recipient as input from user
subject = input("Subject: ")
body = input("Body: ")
recipient = input("Recipient: ")

# adding user provided recipient to the receivers list
receivers.append(recipient)


try:
    # creating a message object of above imported object
    message = MIMEMultipart()
    # Putting from email details to message attributes
    message['From'] = sender
    
    # Putting to email details to message attributes, getting it from receivers list
    message['To'] = receivers[0]
    
    # Putting subject  details to message attributes
    message['Subject'] = subject
    
    # Putting  email body details as text to message attributes
    message['Body'] = body
    
    # Creating session with gmail protocol and providing port for the session
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    
    # adding security packets to session 
    session.starttls() 
    # Making user log in with provided sender email and password
    session.login(sender, password) 
    
    # Sending email through session with sender, receiver and body of email
    session.sendmail(sender, receivers, body)

    # quitting the session
    session.quit()         
    print("Successfully sent email")
except smtplib.SMTPException as e:
   print (e)
