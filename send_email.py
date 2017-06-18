import smtplib
from email.mime.text import MIMEText
import cozmo

GMAIL_USER = <gmail address>
APP_PASSWORD = <gmail password>

def send_email():
    # Send the message via our own SMTP server, but don't include the
    # envelope header.
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(GMAIL_USER, APP_PASSWORD)
    server.sendmail(GMAIL_USER, GMAIL_USER, "Intruder Detected!")
    server.close()
    

def cozmo_program(robot: cozmo.robot.Robot):
    send_email()
    robot.say_text("Email Sent!", use_cozmo_voice=False).wait_for_completed()

cozmo.run_program(cozmo_program)