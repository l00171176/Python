"""
 Script: my_if.py
 By: Shivani Gupta (L00171176)
 Purpose: Python Walkthrough 04: If-Elif-Else Statement
 Tested: Python v3.10.7; Windows 11
 Alpha version: 6th October 2022
"""

#Boolean variables
#test 1
#a=True
#b=True
c=True

#test 2
a=False

#test 3
b=False

#test 4
#c=False

if a:
    print("'a' was True")
elif b:
    print("'b' was True")
elif c:
    print("'c' was True")
else:
    print("None of the boolean variables were True")

#Comparison Operators
if (3>2) and (5<9):
    print("Yup!")
else:
    print("Nope")
