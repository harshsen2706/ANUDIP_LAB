# 2. Write a Python program to get the largest and smallest number from a list without builtin functions. 

# Python program to find the largest and smallest number from a list without builtin functions

# Function to find the largest number in the list
def find_largest(lst):
    # Initialize the first element as the largest
    largest = lst[0]
    
    # Loop through each element in the list
    for num in lst:
        # If the current number is greater than the current largest, update largest
        if num > largest:
            largest = num
    return largest

# Function to find the smallest number in the list
def find_smallest(lst):
    # Initialize the first element as the smallest
    smallest = lst[0]
    
    # Loop through each element in the list
    for num in lst:
        # If the current number is smaller than the current smallest, update smallest
        if num < smallest:
            smallest = num
    return smallest

# Example list
my_list = [10, 20, 5, 40, 1, 35]

# Calling the functions and storing the results
largest = find_largest(my_list)
smallest = find_smallest(my_list)

# Printing the results
print("The largest number in the list is:", largest)
print("The smallest number in the list is:", smallest)



""" ans The largest number in the list is: 40
The smallest number in the list is: 1
"""
