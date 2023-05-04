# Module 06-1 Raptor Logic in Python
# Created by Julian Payne
# Version 1.0 
# Last date of revision: April 30, 2023
# In this program, a user can input ten numbers and be displayed an array
# of those numbers in reversed order. Upon each successful input an array 
# will be updated with those values. Once ten numbers are entered, the 
# reverse_array() function will be called in order to reverse the order of
# the array. Once reversed the array will be outputted to the user.
# Variables include:
# MAX_NUMBERS = numeric constant for maximum number of inputs (data type = integer)
# QUIT = sentinel value to exit the program (data type = string)
# array = empty array to add input to (data type = list)
# count = counter to keep track of amount of inputs (data type = integer)
# number = used to store user input (data type = string)
# length = calculates length of array (data type = integer)
# maxIndex = stores the maximum index and is updated through iterations to 
# reflect the next highest index (data type = integer)
# iterations = calculates number of iterations for the loop (data type = integer)
# storedValue = stores initial value of the maximum index (data type = integer)

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
                reverse_array(array)
        if number == QUIT:
            break

def reverse_array(array):
    length = len(array)
    maxIndex = length - 1
    iterations = int(length / 2)
    for i in range(iterations):
        storedValue = array[maxIndex]
        array[maxIndex] = array[i]
        array[i] = storedValue
        maxIndex -= 1
    print(f"Reversed array: {array}")

housekeeping()