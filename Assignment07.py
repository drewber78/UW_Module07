# ------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Assignment 07 practice code for pickling and error handling;
#           Program takes two user inputted numbers, calculates the sum, difference,
#           product, and quotient, then outputs the results to a binary .dat file.
#           Appends data rather than overwriting the results.
# Changelog (When, Who, What):
# 27FEB2023, Drew Cochran, created initial file and wrote first attempt code
# 28FEB2023, Drew Cochran, Debugged with Kelly Kaufman; fixed errors and made sure code works
# 01MAR2023, Drew Cochran, Completed up top description, committed to Github.
#
#
# -------------------------------------------------------------------------------- #


import pickle

# Variables for use
value1 = 0
value2 = 0
data = []
sum = 0
diff = 0
prod = 0
quot = 0
objFile = "Calculations.dat"


# function to ask user to calculate sum, difference, product, and quotient
def calculation(value1, value2):
    """
    Calculates the sum, difference, product, and quotient. Returns tuple of the calculations
    :param value1:
    :param value2:
    :return:
    """

    sum = value1 + value2
    diff = abs(value1 - value2)
    prod = value1 * value2
    try:
        quot = value1 / value2

    except(ZeroDivisionError):
        print("Cannot divide by zero.")
        quot = None

    return sum, diff, prod, quot

def user_menu():

    """
    Menu for user to input the numbers to calculate for sum, difference, product, and quotient.
    :return: value1 and value2
    """
    try:
        value1 = float(input("Enter the first number to calculate: "))
        value2 = float(input("Enter the second value to calculate: "))

        # if check for user inputted zero in value2
        if value2 == 0.0:
            print("Quotient will be invalid for this calculation as you cannot divide by zero.")
        return value1, value2

    except:

        print("Inputted values must be numbers or float numbers.")
        value1 = 0
        value2 = 0
        return value1, value2

def open_close_pickle_file(data):

    """
    Open and closes the pickle file. Writes the data stored to the file while open.
    :param: data list
    :return:
    """
    objFile = open("Calculations.dat", "ab")
    pickle.dump(data, objFile)
    objFile.close()

def main_processing_function():
    """
    Completes the main processing of the user inputted data.
    :return:
    """

    value1, value2 = user_menu()
    data.append((value1, value2))
    data.append(calculation(value1, value2))
    open_close_pickle_file(data)

main_processing_function()