#!/usr/bin/python3

from datetime import date as dt

def tdminusbd(td, bd):

     thirtyone = False
     thirty= False
     omonth = False
     if bd.month in (1, 3, 5, 7, 8, 10, 12):
         thirtyone=True
         thrity=False
     elif bd.month in (4, 6, 9, 11):
         thirtyone=False
         thrity=True
     else:
         # you weer born in feb
         thirtyone=False
         thrity=False

     if thirtyone :
         print ("there are 31 days in month ", str(bday.month))
     elif thirty :
         print ("there are 30 days in month ", str(bday.month))
     else :
         print ("there are 28 days in month ", str(bday.month))

     if td.day >= bd.day :
          days = td.day - bd.day
          omonth = False
     else :
         omonth = True
         if thirtyone :
              days = td.day + 31 - bd.day
         elif thirty :
             days = td.day + 30 - bd.day
         else :
             days = td.day + 28 - bd.day

     print ("thirtyone is ", str(thirtyone))
     print ("thirty is ", str(thirty))
     print ("owe month is ", str(omonth))

     if omonth :
          months = td.month - bd.month -1
     else :
          months = td.month - bd.month

     years = td.year - bd.year
     age = dt(years, months, days)
     return (age)

today = dt.today()
print("Todays date is, ", today.day)
print("it is the month of, ", today.month)
print("the year is, ", today.year)

bday = dt(1966,1,29)

print (bday.year)
print (bday.month)
print (bday.day)

# tdminusbd(today,bday)
howold = tdminusbd(today,bday)
print ("you are ", howold.day, " days")
print (howold.month, " months")
print (howold.year, " years old.")
