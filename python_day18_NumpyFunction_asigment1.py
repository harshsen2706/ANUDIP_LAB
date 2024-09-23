# 1. Suppose you have a dataset containing daily temperature readings for a city, and you want to identify days with extreme temperature conditions.
# Find days where the temperature either exceeded 35 degrees Celsius (hot day) or dropped below 5 degrees Celsius (cold day). 

import numpy as np

# Input data
temperatures = np.array([32.5, 34.2, 36.8, 29.3, 31.0, 38.7, 23.1, 18.5, 22.8, 37.2,-4,-12])

temp=temperatures[temperatures>35]
print(temp)