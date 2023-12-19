import random
import smtplib
import key
from key import PASSWORD
import datetime as dt

day_of_week = dt.datetime.now()

with open("quotes.txt") as quote_list:
    content = quote_list.readlines()

my_email = "mojojo.aderinto@gmail.com"
my_password = key.PASSWORD

if day_of_week.weekday() == 1:
    quote_of_the_day = random.choice(content)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs="agbako@myyahoo.com",
                            msg=f"subject:Monday Motivations\n\n{quote_of_the_day}")
else:
    print("Not a monday today")