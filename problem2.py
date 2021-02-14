"""
----------------------------------------------------------
Name: problem2.py
Purpose: Allows you to enter your summer earnings and average grade to determine where you will be going this summer!

Author: Yeh.A

Created: 14/02/2021
----------------------------------------------------------
"""
print("***** Where Will You Go This Summer? *****")
print(" ")

#get average grade and earnings before the summer
mark = float(input("Enter your average grade: "))
earnings_before_the_summer = float(input("Enter your earnings before the summer ($): "))

#if mark is higher than 80 and you earned $500 or more it outputs you can go to Europe
if mark >= 80 and earnings_before_the_summer >= 500:
  print("You can go away to Europe!")

#if mark is higher than 80 but you didn't earn $500 or more it outputs you can go to California
elif mark >= 80:
  print("You can go to California!")

#if you didn't get an average of higher than 80 it outputs you can't go anywhere
else: 
  print("You don't get to go away.")