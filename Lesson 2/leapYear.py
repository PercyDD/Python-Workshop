from __future__ import print_function

year = int(input("Enter a year: "))
if (year % 4) == 0:
   if (year % 100) != 0 or (year % 400) == 0:
        print(year,"is a leap year")

    
