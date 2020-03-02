import smtplib
from email.mime.text import MIMEText  # Import classes
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


# Create an object and initialize connection
# Connect with host, port
# Secure our server
# Login to account
def send(filename):
    from_address = 'from email address'
    to_address = 'to email address'
    subject = "Finance Stock Report"

    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = subject
    body = "Today's finance report attached."
    msg.attach(MIMEText(body, 'plain'))  # use 'html' for HTML email

    # Open the file to upload
    my_file = open(filename, 'rb')
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(my_file).read()  # Set payload
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename= ' + filename)
    msg.attach(part)  # attach file

    message = msg.as_string()

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_address, 'password')  # Configure Gmail for one-time application use

    server.sendmail(from_address, to_address, message)

    server.quit()

# TODO store sensitive email information in separate, protected file rather than in app.

