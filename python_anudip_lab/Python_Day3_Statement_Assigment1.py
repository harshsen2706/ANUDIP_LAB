Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # 1. Using input() function take one number from the user and using ternary operators check whether the number is even or odd.
>>> 
>>> # Get input from the user
... number = int(input("Enter a number: "))
Enter a number: 5
>>> 
>>> # Check if the number is even or odd using a ternary operator
... result = "Even" if number % 2 == 0 else "Odd"
>>> 
>>> # Print the result
... print(f"The number {number} is {result}.")
The number 5 is Odd.
>>> 
>>> #ans The number 5 is Odd.
