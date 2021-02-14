"""
----------------------------------------------------------
Name: problem1.py
Purpose: Allows user to enter the three side lengths of a triangle and determine if it is a right-angled triangle or not.

Author: Yeh.A

Created: 14/02/2021
----------------------------------------------------------
"""

print("***** Is it a Right Triangle or Not? *****")
print(" ")

#get side lengths
side_1 = int(input("Enter the length of side 1: "))
side_2 = int(input("Enter the length of side 2: "))
side_3 = int(input("Enter the length of side 3: "))

#compute squares
square_1 = side_1**2
square_2 = side_2**2
square_3 = side_3**2

#use pythagorean theorem to determine if it's a right triangle
if (square_1 + square_2 == square_3) or (square_1 + square_3 == square_2) or (square_2 + square_3 == square_1):
  print("A triangle with side lengths " + str(side_1) + ", " + str(side_2) + ", and " + str(side_3) + " forms a right-angled triangle.")

else:
  print("A triangle with side lengths " + str(side_1) + ", " + str(side_2) + ", and " + str(side_3) + " does not form a right-angled triangle.")