import smtplib

def SendMess(email, mess):
    EMAIL = "initonproj@gmail.com"
    PASS = "wnhoddmrlbjv"
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(EMAIL, PASS)
    server.sendmail(EMAIL, email, mess)
    server.quit()                                           #wnho ddmr lbjv
