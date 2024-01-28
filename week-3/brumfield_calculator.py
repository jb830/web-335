"""""
============================================
; Title:  brumfield_myworld.py 
; Author: Professor Krasso
; Date: 28, January, 2024
; Modified by: Joanna Brumfield
; Description: Pthon Math Functions
;===========================================
"""""

# Create a function named add with two parameters and in the body of the method return the total.
# Create a function named subtract with two parameters and in the body of the method return the subtracted total. 
# Create a function named divide with two parameters and in the body of the method return the divided total.
# Create a function named multiply with two parameters and in the body of the method return the multiplied total.
# Create variables to test each function.  Use a variable to build a string for the results.  Use the format <num1 [arithmetic operation] num2 is num3.  For example, 

# Call each function passing in the variables created in step 6 and print the results to the console window using an output variable and string concatenation.  
#addition function
def add(num1, num2):
    total = num1 + num2
    return total

#subtraction function
def subtract(num1, num2):
    total = num1 - num2
    return total

#division function
def divide(num1, num2):
    total = num1 / num2
    return total

#multiplication function
def multiply(num1, num2):
    total = num1 * num2
    return total
    
#test functions
print(add(10,12))
print(subtract(24,10))
print(divide(24,3))
print(multiply(2,8))