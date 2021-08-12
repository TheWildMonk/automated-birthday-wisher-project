from smtplib import *
from datetime import *
from random import *
import pandas as pd

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
df_birthdays = pd.read_csv("birthdays.csv")
birthday_dict = df_birthdays.to_dict(orient="records")

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




