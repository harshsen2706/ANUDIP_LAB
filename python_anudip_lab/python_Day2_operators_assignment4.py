Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #4. Python program to find the area of a triangle whose sides are given
>>> # Input: Lengths of the sides of the triangle
>>> a = float(input("Enter the length of side a: "))
... 
Enter the length of side a: 4
>>> b = float(input("Enter the length of side b: "))
... 
Enter the length of side b: 5
>>> c = float(input("Enter the length of side c: "))
... 
Enter the length of side c: 6
>>> # Calculate the semi-perimeter (s)
... s = (a + b + c) / 2
>>> KeyboardInterrupt
>>> # Calculate the area using Heron's formula
... area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
... 
>>> # Output: Area of the triangle
... print(f"The area of the triangle is: {area}")
The area of the triangle is: 9.921567416492215
>>> #ans The area of the triangle is: 9.921567416492215
