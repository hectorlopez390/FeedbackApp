import smtplib
from email.mime.text import MIMEText

def send_mail(customer, dealer, rating, comments):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = 'a69cc47630c0c2'
    password = '295009a14d267a'
    message = f"<h3> New Feedback Submission</h3> <ul><li>Customer: {customer}</li><li>Dealer: {dealer}</li><li>Rating: {rating}</li><li>Comments: {comments}</li></ul>"

    sender_email = 'hectorlopez.view@gmail.com'
    receiver_email = 'hectorlopez.view@gmail.com'
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Buick Feedback'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    #send email
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())