#1. Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.


# Python program to handle ZeroDivisionError

try:
    numerator = float(input("Enter the numerator: "))
    denominator = float(input("Enter the denominator: "))
    
    # Trying to divide the two numbers
    result = numerator / denominator
    print(f"Result: {result}")

except ZeroDivisionError:
    # This block will be executed in case of division by zero
    print("Error: Division by zero is not allowed.")


""" ans -->Enter the numerator: 10
         Enter the denominator: 0

         Error: Division by zero is not allowed.
"""
