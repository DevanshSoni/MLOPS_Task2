import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

MESSAGE = MIMEMultipart('alternative')
subject="Error in Your Code"
MESSAGE['subject'] = subject
MESSAGE['To'] = "devanshsoni108@gmail.com"
MESSAGE['From'] = "devanshsoni108@gmail.com"
body="""

Hello Developer There is an <b>Issue in Your code</b> that you've Pushed to <b>Github</b> Last Time<br>
Please, Correct it and <b>Re Push it to Github Again</b>, for further processing.
"""
HTML_BODY = MIMEText(body, 'html')
MESSAGE.attach(HTML_BODY)
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login('devanshsoni108@gmail.com','Soni@Family123')
server.sendmail(
        'devanshsoni108@gmail.com',
        "devanshsoni108@gmail.com",
        MESSAGE.as_string()
    )
server.quit()
