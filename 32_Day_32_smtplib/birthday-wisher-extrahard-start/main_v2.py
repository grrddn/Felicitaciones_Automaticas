##################### VERSION 2 ######################

from datetime import datetime
import pandas as pd
import random
import smtplib

today = datetime.now()
today_tuple = (today.month, today.day)
my_email = "daniel.ortega.leon.mx@gmail.com"
my_password = "emri rjgy pzdz moly"
recipient = ""

data = pd.read_csv(r"C:\Users\lenovo\OneDrive - HOTELERA YALKUITO SA DE CV\Desktop\No Borrar Daniel\32 Web Development\02 Python\32_Day_32_smtplib\birthday-wisher-extrahard-start\birthdays.csv", header=None)
data.columns = ["name", "email", "year", "month", "day"]

data_dict = {
    (data_row["month"], data_row["day"]): data_row
    for (index, data_row) in data.iterrows()
}

if today_tuple in data_dict:
    birthday_person = data_dict[today_tuple]
    file_path = f"C:\\Users\\lenovo\\OneDrive - HOTELERA YALKUITO SA DE CV\\Desktop\\No Borrar Daniel\\32 Web Development\\02 Python\\32_Day_32_smtplib\\birthday-wisher-extrahard-start\\letter_templates\\letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday\n\n{contents}"
        )