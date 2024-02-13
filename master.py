import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def job():
    excel_file = "Sample-OptionalHolidays.xlsx"
    df = pd.read_excel(excel_file)


    tomorrow = pd.Timestamp.now().normalize() + pd.Timedelta(days=1)
    holiday_tomorrow = df[df['Date'] == tomorrow]

    if holiday_tomorrow.empty:
        print("No Optional Holiday tomorrow")
        exit()


    sender_email = "akash.singh2761@gmail.com"
    receiver_email = "akash.singh@geminisolutions.com"
    password = ""


    subject = "Employees Availing Optional Holiday Tomorrow"
    body = "The following employees are availing Optional Holiday tomorrow:\n"
    for index, row in holiday_tomorrow.iterrows():
        body += f"- {row['Employee Name']}\n"


    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com:587')  # Update SMTP server details
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email.split(","), msg.as_string())
    print("Successfully sent the mail.")
    server.quit()

import schedule
import time

# def job():
#     print("Running the job...")
#     import master

schedule.every(40).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)