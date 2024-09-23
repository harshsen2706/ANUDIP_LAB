# 2.Suppose you have two sets of employee data—one containing information about full-time employees
# and another containing information about part-time employees. You want to combine this data to create a comprehensive employee dataset for HR analysis. 

import numpy as np

# Full-time employee data
full_time_employees = np.array([
    [101, 'John Doe', 'Full-Time', 55000],
    [102, 'Jane Smith', 'Full-Time', 60000],
    [103, 'Mike Johnson', 'Full-Time', 52000]
])

# Part-time employee data
part_time_employees = np.array([
    [201, 'Alice Brown', 'Part-Time', 25000],
    [202, 'Bob Wilson', 'Part-Time', 28000],
    [203, 'Emily Davis', 'Part-Time', 22000]
])

# Combine the datasets using np.vstack: This function vertically stacks the two arrays, effectively combining them into one.
combined_employees = np.vstack((full_time_employees, part_time_employees))

# Printing the result
print("Combined Employee Data:")
print(combined_employees)

#output
"""
Combined Employee Data:
[['101' 'John Doe' 'Full-Time' '55000']
 ['102' 'Jane Smith' 'Full-Time' '60000']
 ['103' 'Mike Johnson' 'Full-Time' '52000']
 ['201' 'Alice Brown' 'Part-Time' '25000']
 ['202' 'Bob Wilson' 'Part-Time' '28000']
 ['203' 'Emily Davis' 'Part-Time' '22000']]


"""

