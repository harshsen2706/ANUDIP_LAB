
#3. Write a Python program to find duplicate values from a list and display those


# Python program to find and display duplicate values from a list

def find_duplicates(lst):
    # Empty list to store duplicate values
    duplicates = []
    
    # Loop through each element in the list
    for i in range(len(lst)):
        # Compare the current element with all the other elements
        for j in range(i + 1, len(lst)):
            # If a duplicate is found and not already in the duplicates list, add it
            if lst[i] == lst[j] and lst[i] not in duplicates:
                duplicates.append(lst[i])
    
    return duplicates

# Example list with duplicate values
my_list = [10, 20, 30, 20, 40, 10, 50, 60, 30]

# Calling the function and storing the result
duplicates = find_duplicates(my_list)

# Printing the duplicates
print("Duplicate values in the list are:", duplicates)


#ans Duplicate values in the list are: [10, 20, 30]
