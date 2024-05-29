import random
import smtplib
# import key
import datetime as dt

# from key import PASSWORD
day_of_week = dt.datetime.now()
with open("quotes.txt") as quote_list:
    content = quote_list.readlines()
    print(random.choice(content))
    print(day_of_week)

if day_of_week.weekday() == 1
    my_email = "mojojo.aderinto@gmail.com"
    my_password = key.PASSWORD
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(from_addr=my_email, to_addrs="agbako@myyahoo.com", msg="Hello again")




