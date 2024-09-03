#2.Write a Python program to remove a newline in Python String = "\nBest \nDeeptech \nPython \nTraining\n"


# Given string with newline characters
string = "\nBest \nDeeptech \nPython \nTraining\n"

# Remove newlines using replace method
string_no_newlines = string.replace("\n", " ")

# Or, you can use splitlines and join method
# string_no_newlines = " ".join(string.splitlines())

# Remove extra spaces that may be added at the start and end
string_no_newlines = string_no_newlines.strip()

# Print the result
print(string_no_newlines)

#ans Best Deeptech Python Training
