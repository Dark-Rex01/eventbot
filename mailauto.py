import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="test"
)
mycursor = conn.cursor()
mycursor1 = conn.cursor()
mycursor2 = conn.cursor()
mycursor3 = conn.cursor()
mycursor4 = conn.cursor()


mycursor.execute("SELECT `id`,`name`, `website` FROM users")
myresult = mycursor.fetchall()
mycursor1.execute("SELECT name FROM users")
myresult1 = mycursor1.fetchall()
mycursor2.execute("SELECT mail FROM mail")
myresult2 = mycursor2.fetchall()
mycursor3.execute("SELECT title FROM mailcon")
myresult3 = mycursor3.fetchall()

for x in myresult:
    a = x[0]
    c = x[1]
    e = x[2]
    for z in myresult3:
        b = z[0]
        if a == b:
                mail_content = "hi, here is an you might be interested in a event named " + a + "\n date:" + c + "\n website link:" + e
                print(a)
                mycursor4.execute("DELETE FROM `mailcon` WHERE `title`= %s && `date`=%s ", [a,c])
                conn.commit()
                sender_address = 'vishalbond547@gmail.com'
                sender_pass = '0007vishal'
                for y in myresult2:
                    rec = y[0]
                    receiver_address = rec
                    # Setup the MIME
                    message = MIMEMultipart()
                    message['From'] = sender_address
                    message['To'] = receiver_address
                    message['Subject'] = 'event announcement'  # The subject line
                    # The body and the attachments for the mail
                    message.attach(MIMEText(mail_content, 'plain'))
                    # Create SMTP session for sending the mail
                    session = smtplib.SMTP('smtp.gmail.com', 587)
                    session.starttls()  # enable security
                    session.login(sender_address, sender_pass)
                    text = message.as_string()
                    session.sendmail(sender_address, receiver_address, text)
                    session.quit()
                    print('Mail Sent')
        else:
            print("already sent")
