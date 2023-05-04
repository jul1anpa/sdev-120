# Module 04-2 Raptor Logic in Python
# Created by Julian Payne
# Version 1.0 
# Last date of revision: April 26, 2023
# This program will accept three number inputs from a user.
# If the sum of the first two inputs equals the third input a
# message will be outputed to the user. If not then no message 
# will appear and the program will end.
# Variables include:
# firstnum = first user input with data type integer
# secondnum = second user input with data type integer
# thirdnum = third user input with data type integer

firstnum = int(input("Enter first number: "))
secondnum = int(input("Enter second number: "))
thirdnum = int(input("Enter third number: "))

if firstnum + secondnum == thirdnum:
    print("The sum of the first and second numbers equals the third number.")
elif secondnum + thirdnum == firstnum:
    print("The sum of the second and third numbers equals the first number.")
else:
    print("The sum of the first and third numbers equals the second number.")