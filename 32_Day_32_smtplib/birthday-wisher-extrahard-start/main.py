##################### VERSION 1 ######################

import datetime as dt
import pandas as pd
import smtplib
import random

my_email = "daniel.ortega.leon.mx@gmail.com"
my_password = "emri rjgy pzdz moly"
recipient = ""
file_path = r"C:\Users\lenovo\OneDrive - HOTELERA YALKUITO SA DE CV\Desktop\No Borrar Daniel\32 Web Development\02 Python\32_Day_32_SMTPLIB\birthday-wisher-extrahard-start\birthdays.csv"

today = dt.datetime.now().month, dt.datetime.now().day
month = today[0]
day = today[1]

letter_1 = r"C:\Users\lenovo\OneDrive - HOTELERA YALKUITO SA DE CV\Desktop\No Borrar Daniel\32 Web Development\02 Python\32_Day_32_SMTPLIB\birthday-wisher-extrahard-start\letter_templates\letter_1.txt"
letter_2 = r"C:\Users\lenovo\OneDrive - HOTELERA YALKUITO SA DE CV\Desktop\No Borrar Daniel\32 Web Development\02 Python\32_Day_32_SMTPLIB\birthday-wisher-extrahard-start\letter_templates\letter_2.txt"
letter_3 = r"C:\Users\lenovo\OneDrive - HOTELERA YALKUITO SA DE CV\Desktop\No Borrar Daniel\32 Web Development\02 Python\32_Day_32_SMTPLIB\birthday-wisher-extrahard-start\letter_templates\letter_3.txt"

letters = [letter_1, letter_2, letter_3]
random_letter = random.choice(letters)


try:
    with open(file_path, "r") as file:
        df = pd.read_csv(file, header=None)
        df = pd.DataFrame(df)
        df.columns = ["name", "email", "year", "month", "day"]
        for i in range(len(df)):
            if month == df["month"][i] and day == df["day"][i]:
                recipient = df["email"][i]
                with open(random_letter, "r") as file:
                    letter = file.read()
                    letter = letter.replace("[NAME]", df["name"][i])
                    with smtplib.SMTP("smtp.gmail.com", 587) as connect:
                        # this line is for security
                        connect.starttls()
                        # this line is for login
                        connect.login(my_email, my_password)
                        connect.sendmail(from_addr=my_email, to_addrs=recipient, msg=f"Subject: HAPPY BIRTHDAY\n\n{letter}")
                        print("Email sent successfully!") 
except Exception as e:
    print("An error occurred:", e)




