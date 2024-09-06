#2. Write a Python program to remove duplicate characters of a given string.Input = “String and String Function” Output: String and Function


def remove_duplicates(input_string):
    seen = set()
    output_string = []
    
    for char in input_string:
        if char not in seen:
            seen.add(char)
            output_string.append(char)
    
    return ''.join(output_string)

# Given input string
input_string = "String and String Function"
output_string = remove_duplicates(input_string)

print("Output:", output_string)


#ans Output: String adFuc
