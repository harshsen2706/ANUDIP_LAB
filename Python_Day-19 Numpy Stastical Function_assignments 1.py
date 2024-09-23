#1.Compute the median of the flattened NumPy array 

#  Input: x_odd = np.array([1, 2, 3, 4, 5, 6, 7])



import numpy as np  # Importing the NumPy library

# Given array
x_odd = np.array([1, 2, 3, 4, 5, 6, 7])  # Creating a NumPy array with odd number of elements

# Compute the median of the flattened array
# np.median() calculates the median value of the array
median_value = np.median(x_odd)

# Output the result
print("Median of the array:", median_value)  # Printing the median value



#ans Median of the array: 4.0
