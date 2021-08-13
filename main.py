import os
import random
import smtplib
import datetime as dt
import pandas as pd

# Emails & password
email = "demo@email.com"
password = "##########"

# Create a dictionary from birthdays.csv
df_birthdays = pd.read_csv("birthdays.csv")
birthday_dict = df_birthdays.to_dict(orient="records")

# Check whether any birthday matches today's date
today = dt.datetime.today()
for name in range(len(birthday_dict)):
    if today.month == birthday_dict[name]["month"] and today.day == birthday_dict[name]["day"]:
        receiver = birthday_dict[name]["email"]

        # Choose a random letter from letter_templates directory
        letter_template = random.choice(os.listdir("letter_templates"))
        with open(f"letter_templates/{letter_template}") as data_file:
            data = data_file.read()
        letter = data.replace("[NAME]", birthday_dict[name]["name"])

        # Send the birthday wish email
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=email, password=password)
            connection.sendmail(from_addr=email, to_addrs=receiver, msg=f"subject: HAPPY BIRTHDAY!!!\n\n"
                                                                        f"{letter}")
