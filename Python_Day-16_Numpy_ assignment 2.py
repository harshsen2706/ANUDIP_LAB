#2. Convert the below list into a numpy array then display the array then display the first and last index and then multiply each element by 2 and display the result.

#Input: my_list = [1, 2, 3, 4, 5].


import numpy as np

# Input list
my_list = [1, 2, 3, 4, 5]

# Convert list to numpy array
np_array = np.array(my_list)

# Display the array
print("Array:", np_array)

# Display first and last index
print("First index element:", np_array[0])
print("Last index element:", np_array[-1])

# Multiply each element by 2
multiplied_array = np_array * 2

# Display the result
print("Array after multiplying each element by 2:", multiplied_array)

#ans Array: [1 2 3 4 5]
#First index element: 1
#Last index element: 5
#Array after multiplying each element by 2: [ 2  4  6  8 10]

