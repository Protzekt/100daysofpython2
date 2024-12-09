import smtplib
#
# my_email = "testing@gmail.com"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user= pass, password= pass)
#     connection.sendmail(
#         from_addr= " "
#         to_addrs= " "
#         msg= " "
#     )
#

import random

import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# print(now)
# print(year)
# date_of_birth = dt.datetime(year=2002, month=10, day=21)
# print(date_of_birth)

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote =  random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASS)
        connection.sendmail(from_addr= " ",to_addrs= " ", msg=f" ")
