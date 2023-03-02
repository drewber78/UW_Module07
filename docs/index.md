# Pickling and Try-Except Error Handling  
**Dev:** *Drew Cochran*  
**Date:** *01MAR2023*

# Introduction  
This is the seventh assignment for the Python Fundamentals course. This one was a bit stressful for me, though I got some good help from Kelly with my code. I am glad this assignment is done, thank goodness, as I am not that confident in what we were supposed to do. Still, good help always is a great thing.

# Pickling  
Pickling is an interesting topic. It makes sense to use this since everything in computing is in bits anyway. Storing the data in binary for speed and ease of opening, closing, and transferring just makes sense. The website I found that really helped me is located at the bottom of this paragraph. The guy was very good at showing how simple using pickling is and what to do with it. Randal’s video was good too, but this one seemed to make it simple. The only issue I had with how the guy did it was he said the file needed to be .pickle, which didn’t work for me. Perhaps I need a Windows11 add-on to recognize .pickle or something else, but Python could not find the file nor was it recognizing a .pickle file was being called. Once Kelly showed me it needs to be .dat, then my code worked just fine.

https://pythonprogramming.net/python-pickle-module-save-objects-serialization/

# Try-Except  
This was a great review for me as, while I have some experience in this, I don’t know all of the best ways to use it. Randal’s description helped out a lot, specifically how we should use a Try Except block whenever humans are involved. This is a great way to look at coding since it helps when a user screws things up or, rather how things that operate around a user, it will show there is an error and that the error is located in a specific spot. As for a website that also helped, the https://pythonbasics.org/try-except/ website gave me great examples, especially when it comes to using finally.

# Creating Custom Exception classes  
This is a complicated issue for me. It is difficult for me to understand why you want to do this. I guess it is a way to reuse the Exception class over and over again, though I don’t know if there is also a way to identify where the error was located in the first place. I suppose you can put that in the exception to print out or store in an error variable or something like that. I need to explore this more, though I have a feeling we will be using this in next couple of assignments. In previous courses, I have used this because I was told to do so, but I haven’t done it yet by choice.

# Creating A Markdown File  
Creating a markdown (.md) file was a bit dauting. As of writing this, I haven’t done this yet, but I am rewatching Randal’s video on it. I believe it is just going to take some time to play with it. For the most part, I feel it is just some tweaks and playing around that I need to do, then I will get the hang of it.

# Script Assignment  
For this assignment, I was trying to think of ways to use pickling and the try-except, but nothing was coming to mind for the longest time. Then I thought back to assignment 06 and the labs, specifically calculating the sum, difference, product, and quotient lab. This seemed like a great and easy way to get a user to input something and then show it as an output on screen and in a file. See Figures 1 and 2 for the output.

!,[Figure 1. Running In Command Terminal](https://github.com/drewber78/UW_Module07/blob/master/docs/images/Code%20in%20command%20terminal.png "Figure1. Running in Command Terminal")  
**Figure 1. Running In Command Terminal**  

!,[Figure 2. Running in PyCharm](https://github.com/drewber78/UW_Module07/blob/master/docs/images/Code%20in%20pycharm%20terminal.png "Figure2. Running in PyCharm")
**Figure 2. Running in PyCharm**  

For my code in pickling, what I decided to do was use a function to handle all of the opening and closing of the file to then write the final calculation data to the file and then close. I didn’t create a while loop, either, to have the user input multiple numbers to calculate since that was not the intent that I wanted to have. I mainly was thinking this could be a program where I could remove the user inputs and pass data from another source into to get the calculations I wanted in an automated way, then write it all one at a time to a file. See Figure 3 for examples of my pickling code.

```  
def open_close_pickle_file(data):

    """
    Open and closes the pickle file. Writes the data stored to the file while open.
    :param: data list
    :return:
    """
    objFile = open("Calculations.dat", "ab")
    pickle.dump(data, objFile)
    objFile.close()
```  
For my Try-Except, I chose, after confirming with Kelly, to place it in my user menu function. I also chose to place one to help with divide by zero errors and to tell users what happens and there won’t be data if the user inputs 0 as the second number. See below for examples.

```  
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
```  
``` 
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
```  
# Conclusion  
I was a bit apprehensive about this assignment. I was glad it is over since I wanted to get started on Assignment 8. Specifically, I was happy to learn about Try-Except more and especially how to pickle items. Keep it coming for Assignment 8!
