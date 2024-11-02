#2: Suppose you want to track and analyze your household expenses for a month. You have recorded the expenses for various categories, such as groceries, utilities, rent, transportation, and entertainment. You can represent this expense data using a Pandas Series. 

#Input: # Expense categories

#categories = ['Groceries', 'Utilities', 'Rent', 'Transportation', 'Entertainment']

# Monthly expense data (example data in USD) 

#expenses = [500, 200, 1200, 300, 150]



# Step 1: Import the Pandas library
import pandas as pd

# Step 2: Define the list of student names and their exam scores
students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah', 'Ivy', 'Jack']
exam_scores = [92, 88, 76, 94, 82, 90, 85, 89, 78, 91]

# Step 3: Create a Pandas Series using the exam scores and assign the student names as the index
# This allows us to easily access scores by student names
scores_series = pd.Series(exam_scores, index=students)

# Step 4: Display the Series
print(scores_series)




#ans Groceries          500
#Utilities          200
#Rent              1200
#Transportation     300
#Entertainment      150
#dtype: int64
