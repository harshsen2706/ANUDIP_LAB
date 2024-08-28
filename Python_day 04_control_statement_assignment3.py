Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #3.Write a Python program that determines if a given year is a leap year or not.
... 
>>> 
>>> # Get the year from the user
... year = int(input("Enter a year: "))
Enter a year: 2001
>>> 
>>> # Check if the year is a leap year
... if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
...     print(f"{year} is a leap year.")
... else:
...     print(f"{year} is not a leap year.")
... 
...     
2001 is not a leap year.
>>> 
>>> #ans 2001 is not a leap year.
... 
