#1: Suppose you are a teacher, and you want to analyze the exam scores of your students in a particular subject. You have recorded the scores of your students for a recent exam, and you want to represent this data using a Pandas Series.

#Input: students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah', 'Ivy', 'Jack']

#exam_scores = [92, 88, 76, 94, 82, 90, 85, 89, 78, 91]



#Step 1: Import the Pandas library
import pandas as pd

# Step 2: Define the list of student names and their exam scores
students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah', 'Ivy', 'Jack']
exam_scores = [92, 88, 76, 94, 82, 90, 85, 89, 78, 91]

# Step 3: Create a Pandas Series using the exam scores and assign the student names as the index
# This allows us to easily access scores by student names
scores_series = pd.Series(exam_scores, index=students)

# Step 4: Display the Series
print(scores_series)

