import smtplib
import datetime as dt
import random

# Email credentials
my_email = "daniel.ortega.leon.mx@gmail.com"
my_password = "emri rjgy pzdz moly"
recipient = "daniel.ortega_mx@outlook.com"

# Check if it is Wednesday
is_it_wednesday = dt.datetime.now().weekday()
if is_it_wednesday == 2:
    print("It is Wednesday")
    with open(r"C:\Users\lenovo\OneDrive - HOTELERA YALKUITO SA DE CV\Desktop\No Borrar Daniel\32 Web Development\02 Python\32_Day_32_SMTPLIB\Birthday+Wisher+(Day+32)+start\Birthday Wisher (Day 32) start\quotes.txt") as file:
        quotes = file.readlines()
    random_quote = random.choice(quotes) 
    print(random_quote)
    with smtplib.SMTP("smtp.gmail.com", 587) as connect:
        # this line is for security
        connect.starttls()
        # this line is for login
        connect.login(my_email, my_password)
        connect.sendmail(from_addr=my_email, to_addrs=recipient, msg=f"Subject: Test\n\nThis is a test email\n\n{random_quote}")
        print("Email sent successfully!")  
else:
    print("It is not Wednesday")




 
