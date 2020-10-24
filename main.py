import smtplib, ssl
import time
from getpass import getpass

sender_email = input("Enter Your Email : ")
pas = getpass("Password [Hidden] : ") # Password is hidden
receiver_email = input("Enter Recver Email : ")
subject = input("Enter Subject : ")
message = input("Enter Subject : ")
smtp = "smtp.gmail.com" # Default value of smtp
res = []

message = f"Subject: {subject} \n Message: {message}"

def validEmail(email,lst):
    index_check = ""

    i = len(email)
    if i >= 50:
        print("Long Email")
        warn = input("Do you want to continue anyways, it will proccess a little more cpu . [y/n]: ")
        if warn == "y":
            pass
        else:
            exit(0)
    for i in email:
        while (i == '@'):
            if (i=='@'):
                lst.append("success")   
                break             
        while (i == '.'):
            if (i=='.'):
                lst.append("success")
                break
    try:
        lst = lst[1]
        index_check = "valid"
    except IndexError:
        index_check = "invalid"
    return(index_check)

valid = validEmail(sender_email, res)


def check_smtp(email):
    try:
        smtpSplit = email.split("@")
        smtp_provider = smtpSplit[1]
        smtp = f"smtp.{smtp_provider}"
    except IndexError:
        print("Invalid Email !")
        exit(0)
    return smtp

smtp = check_smtp(sender_email)

def send_email(receiver_email, email, pas, validity, smtp, message):
    if validity == "valid":
        pass
    else:
        print("Try after entering a valid email")
        time.sleep(4.0)
        exit(0)
    msg = message
    smtp_server = smtp
    port = 587 
    sender_email = email
    password = pas

    context = ssl.create_default_context()

    try:
        server = smtplib.SMTP(smtp_server,port)
        server.ehlo() 
        server.starttls(context=context) 
        server.ehlo()
        server.login(receiver_email, password)
        server.sendmail(receiver_email, sender_email, msg)
    except Exception as e:
        print(e)
    finally:
        server.quit()
        print("Successfully sent email !")

if __name__ == "__main__":
    try:
        send_email(receiver_email, sender_email ,pas, valid, smtp, message)
    except Exception as error:
        print(f"Failed Due To : {error}")