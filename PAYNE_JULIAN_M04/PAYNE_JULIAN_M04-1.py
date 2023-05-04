# Module 04-1 Raptor Logic in Python
# Created by Julian Payne
# Version 1.0 
# Last date of revision: April 26, 2023
# This program will accept two number inputs from a user
# and determine which number is larger or if they are equal.
# Depending on which of these conditions is satisfied, a 
# corresponding message will be outputed to the user.
# Variables include:
# firstnum = first user input with data type integer
# secondnum = second user input with data type integer

firstnum = int(input("Enter first number: "))
secondnum = int(input("Enter second number: "))

if firstnum == secondnum:
    print("Numbers are equal")
else:
    if firstnum > secondnum:
        print("First is larger")
    else:
        print("Second is larger")
    