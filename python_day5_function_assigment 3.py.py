# 3. Using max() and min() functions display the maximum and minimum of 5 random numbers.


import random

# Generate 5 random numbers
random_numbers = [random.randint(1, 100) for _ in range(5)]


# Find the maximum and minimum of the 5 random numbers
maximum_number = max(random_numbers)
minimum_number = min(random_numbers)


# Display the random numbers, maximum, and minimum
print("The 5 random numbers are:", random_numbers)
print("The maximum number is:", maximum_number)
print("The minimum number is:", minimum_number)


#ans The 5 random numbers are: [58, 9, 8, 60, 12]
#    The maximum number is: 60
#    The minimum number is: 8
