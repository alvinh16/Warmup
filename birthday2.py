#!/usr/bin/python3

from datetime import date as dt

def tdminusbd(td, bd):

     days = td.day - bd.day
     months = td.month - bd.month
     years = td.year - bd.year
#     print ("you are ", days, " days ", months, " months ", years, " years old.")

     age = dt(years, months, days)
     return (age)

today = dt.today()
print("Todays date is, ", today.day)
print("it is the month of, ", today.month)
print("the year is, ", today.year)

bday = dt(1966,1,2)

print (bday.year)
print (bday.month)
print (bday.day)

if bday.month in (1, 3, 5, 7, 8, 10, 12):
    thirtyone=True
    thrity=False
elif bday.month in (4, 6, 9, 11):
    thirtyone=False
    thrity=True
else:
    thirtyone=False
    thrity=False

if thirtyone :
    print ("there are 31 days in month ", str(bday.month))
elif thirty :
    print ("there are 30 days in month ", str(bday.month))
else :
    print ("there are 28 days in month ", str(bday.month))


if (bday.day > today.day):
    print ("yes")
else:
    print ("over")

howold = tdminusbd(today,bday)
print ("you are ", howold.day, " days")
print (howold.month, " months")
print (howold.year, " years old.")
