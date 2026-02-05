"""
1. (SE)
Write a function that takes a number as a parameter and returns 
True if a number can be divided by 3 or 5, otherwise it returns False.

Then write a unit test that checks how the function works (5  cases). 
All the code in Python.
"""

def is_divisible_by_3_or_5(num):
    if num % 3 == 0 or num % 5 == 0:
        return True
    else:
        return False
    

