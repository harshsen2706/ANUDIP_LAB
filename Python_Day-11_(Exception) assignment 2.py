#2. Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.

# Python program to handle invalid integer input

try:
    user_input = input("Enter an integer: ")
    
    # Try to convert the input to an integer
    user_integer = int(user_input)
    
    print(f"Valid integer entered: {user_integer}")

except ValueError:
    # This block will be executed if the input is not a valid integer
    print("Error: Invalid input. Please enter a valid integer.")

"""
ans Enter an integer: hello
Error: Invalid input. Please enter a valid integer.
"""
