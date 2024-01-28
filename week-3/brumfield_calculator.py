"""""
============================================
; Title:  brumfield_myworld.py 
; Author: Professor Krasso
; Date: 28, January, 2024
; Modified by: Joanna Brumfield
; Description: Pthon Math Functions
;===========================================
"""""

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
    
#create variables to test and print functions
num1 = 30
num2= 10

addition = add(num1, num2)
subtraction = subtract(num1,num2)
division = divide(num1,num2)
multiplication = multiply(num1,num2)

print(f"{num1} plus {num2} is {addition}")
print(f"{num1} minus {num2} is {subtraction}")
print(f"{num1} divived by {num2} is {division}")
print(f"{num1} multiplied by {num2} is {multiplication}")