#1. Write a Python program to Count all letters, digits, and special symbols from the given stringInput = “P@#yn26at^&i5ve” Output: Chars = 8 Digits = 2 Symbol = 3

# Given input string
input_string = "P@#yn26at^&i5ve"

# Initialize counters
char_count = 0
digit_count = 0
symbol_count = 0

# Iterate over each character in the string
for char in input_string:
    if char.isalpha():  # Check if the character is a letter
        char_count += 1
    elif char.isdigit():  # Check if the character is a digit
        digit_count += 1
    else:  # If it's neither a letter nor a digit, it's a special symbol
        symbol_count += 1

# Print the results
print(f"Chars = {char_count}")
print(f"Digits = {digit_count}")
print(f"Symbols = {symbol_count}")

""" ans Chars = 8
        Digits = 3
        Symbols = 4

        """
