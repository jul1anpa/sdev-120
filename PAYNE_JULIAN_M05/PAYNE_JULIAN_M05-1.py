# Module 05-1 Raptor Logic in Python
# Created by Julian Payne
# Version 1.0 
# Last date of revision: April 26, 2023
# In this program, the user will be prompted to enter a number.
# The program will then enter a loop that will iterate over a range of numbers
# up to the entered number. For each iteration, the number will be cubed and then 
# assigned to the cubed variable. This variable will then be added to the sum variable
# which will store the sum of each cubed iteration. Upon completion of the final iteration
# within the range, the sum will be outputed to the user. 
# Variable include:
# userinput = the user input that will act as the argument for the range function
# within the loop (data type = integer)
# sum = initialized as 0 this variable will accumulate the sum of each cubed number
# within the desired range (data type = integer)
# cubed = this will store each cubed iteration of the desired range

userinput = int(input("Enter a number: "))
sum = 0

# In Python, the range function will iterate up to the argument.
# For example range(3) will iterate over 0, 1, and 2 but not 3 itself.
# For the purpose of this program I have added 1 to the userinput in order
# to return the desired output.
for number in range(userinput + 1):
    cubed = number ** 3
    sum += cubed

print(sum)