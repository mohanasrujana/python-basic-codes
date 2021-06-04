import smtplib
from email.mime.text import MIMEText

body = "This is a test email.How are you? \n This message is sent without using gmail."

msg = MIMEText(body)
msg['From'] = "mohanasrujana@gmail.com"
msg['To'] = "mohanasrujana@gmail.com"
msg['Subject'] = "Random mail."

server = smtplib.SMTP('smtp.gmail.com',587)

server.starttls()

server.login("mohanasrujana@gmail.com","tonystark3000")

server.send_message(msg)

print("Mail sent")

server.quit()

