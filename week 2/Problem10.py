import time
import datetime
import calendar

tdy=datetime.datetime.today()
print("current date and time = " ,tdy)
print('Month: ', tdy.month)
print('current day of the week: ', tdy.isoweekday())
print('current day of the week: ', tdy.weekday())
tdelta=datetime.timedelta(days= 5)
print("today's date - 5= ",tdy - tdelta)
print("today's date + 5= ",tdy + tdelta)
