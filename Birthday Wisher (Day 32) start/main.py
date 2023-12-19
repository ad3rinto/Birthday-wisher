import smtplib
from dotenv import load_dotenv
load_dotenv()


my_email = "mojojo.aderinto@gmail.com"
my_password = os.environ("PASSWORD")
connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=my_password)
connection.sendmail(from_addr=my_email, to_addrs="agbako@myyahoo.com", msg="Hello again")
