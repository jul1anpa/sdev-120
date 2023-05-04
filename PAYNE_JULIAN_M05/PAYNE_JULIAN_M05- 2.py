# Module 05-2 Raptor Logic in Python
# Created by Julian Payne
# Version 1.0 
# Last date of revision: April 26, 2023
# In this program, the user will be prompted to enter a number or 0 
# to exit the program. Upon entering a number that is not 0, the program
# will enter a loop that will keep prompting the user for a number until they
# exit the loop by entering a 0. With each input, the program will store the 
# input in the userinput variable which will then be added to the sum variable. 
# Once the loop exits via a 0 input, the sum variable will then be outputed.
# Variables include:
# userinput = this variable will store the user's input and will be updated
# each loop iteration (data type = integer)
# sum = this variable is initialized to 0 and will be updated to reflect the 
# sum of each input that the user enters

userinput = int(input("Enter a number or 0 to exit the program: "))
sum = 0

while userinput != 0:
    sum += userinput
    userinput = int(input("Enter a number or 0 to exit the program: "))

print(sum)
