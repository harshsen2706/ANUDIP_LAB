#1. Write a NumPy program to create an array of 10 zeros, 10 ones, and 10 fives

import numpy as np

# Creating an array of 10 zeros
zeros = np.zeros(10)  # [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]

# Creating an array of 10 ones
ones = np.ones(10)  # [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]

# Creating an array of 10 fives
fives = np.full(10, 5)  # [5. 5. 5. 5. 5. 5. 5. 5. 5. 5.]

# Concatenating all three arrays into one
result = np.concatenate([zeros, ones, fives])

# Printing the final array
print(result)


#ans [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 5. 5. 5. 5. 5. 5. 5. 5. 5. 5.]
