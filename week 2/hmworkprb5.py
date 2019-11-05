import datetime
import time
import calendar

bday = datetime.date(1996, 2, 14)
tdy = datetime.date.today()

print("my bithday date is: ",bday)
print("my bithday year is: ",bday.year)
print("my bithday month is: ",bday.month)
print("my bithday day is: ",bday.day)
print("my bithday weekday is: ",bday.weekday())

next_bday = datetime.date(2020, 2, 14)
tdy = datetime.date.today()
till_bday = next_bday - tdy
print("days left to my bday: ", till_bday)

print (calendar.month(2017, 5))

today = datetime.date.today()
tdelta = datetime.timedelta(days=1)
yesterday = tdy - tdelta

print ("yesterday date: ",yesterday)
print ("2 days added to yesterday: ", yesterday + tdelta * 2)
print ("3 days substracted from yesterday: ", yesterday - tdelta * 3)
