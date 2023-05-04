# Module 06-2 Raptor Logic in Python
# Created by Julian Payne
# Version 1.0 
# Last date of revision: April 30, 2023
# In this program, a user can input ten numbers and receive an output
# of all of the numbers along with the largest and smallest numbers among them.
# Upon each successful input an array will be updated with those values. 
# Once ten numbers are entered, the summary() function will be called in order
# to calculate the largest and smallest values within the array. Upon completion,
# the full array along with those values will be outputted. 
# Variables include:
# MAX_NUMBERS = numeric constant for maximum number of inputs (data type = integer)
# QUIT = sentinel value to exit the program (data type = string)
# array = empty array to add input to (data type = list)
# count = counter to keep track of amount of inputs (data type = integer)
# number = used to store user input (data type = string)
# length = calculates length of array, used as range ceiling in loop (data type = integer)
# maxValue = initialized at 0 and updated with values from the array (data type = integer)
# minValue = initialized at 0 and updated with values from the array (data type = integer)

def housekeeping():
    MAX_NUMBERS = 10
    QUIT = "XXX"
    array = []
    count = 0
    print("Enter ten numbers or XXX to exit the program.")
    for i in range(MAX_NUMBERS):
        number = input(f"Enter number {i + 1}: ")
        if number.isdigit():
            count += 1
            array.append(int(number))
            if count == 10:
                summary(array)
        if number == QUIT:
            break

def summary(array):
    array = array
    length = len(array)
    maxValue = 0
    minValue = 0
    for i in range(length):
        if minValue == 0:
            minValue = array[i]
        if array[i] > maxValue:
            maxValue = array[i]
        if array[i] < minValue:
            minValue = array[i]
    print(f"Your numbers: {array}")
    print(f"Largest: {maxValue}")
    print(f"Smallest: {minValue}")

housekeeping()