#1. Write a Python program to count the occurrences of each word in a given sentenc = “To change the overall look of your document. To change the look available in the gallery”


# Given string
sentence = "To change the overall look of your document. To change the look available in the gallery"

# Convert the sentence to lowercase to make the count case-insensitive
sentence = sentence.lower()

# Replace punctuation with spaces
sentence = sentence.replace(".", "")

# Split the sentence into words
words = sentence.split()

# Create an empty dictionary to store word counts
word_count = {}

# Count the occurrences of each word
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Print the word counts
for word, count in word_count.items():
    print(f"{word}: {count}")
    

""" ans
to: 2
change: 2
the: 3
overall: 1
look: 2
of: 1
your: 1
document: 1
available: 1
in: 1
gallery: 1
"""
