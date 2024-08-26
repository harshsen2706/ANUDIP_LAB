Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #2. Using input function take two number and then swap the number
>>> 
>>> # Take two numbers as input from the user
>>> num1 = input("Enter the first number: ")
... 
Enter the first number: 6
>>> 
>>> num2 = input("Enter the second number: ")
... 
Enter the second number: 9
>>> 
>>> # Print the original values before swapping
... 
>>> print(f"Before swapping: num1 = {num1}, num2 = {num2}")
... 
Before swapping: num1 = 6, num2 = 9
>>> 
>>> # Swap the numbers
... 
>>> num1, num2 = num2, num1
... 
>>> # Print the swapped values
... 
>>> print(f"After swapping: num1 = {num1}, num2 = {num2}")
After swapping: num1 = 9, num2 = 6
>>> 
>>> #ans After swapping: num1 = 9, num2 = 6
... 
