# Author: Andrew Shanahan
# A program that outputs whether or not today is a weekday.
# I have included the commands for todays date and an additional request for the year.
# I have given command for requesting what day it is to day as: print (x.strftime("%A")) and equalled to a.
# Date Reference: https://www.w3schools.com/python/python_datetime.asp
# If/else Reference: https://www.w3schools.com/python/python_conditions.asp
import datetime
x = datetime.datetime.now ()
print (x)
print (x.year)
a = (x.strftime("%A"))
b = ("It is the weekend, yay!")
c = ("Yes, unfortunately today is a weekday.")
d = ("Saturday")
e = ("Sunday")
print (b) if a == "Saturday" or "Sunday" else print (c)