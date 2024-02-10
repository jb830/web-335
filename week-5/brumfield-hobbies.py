"""""
============================================
; Title:  brumfield_hobbies.py 
; Author: Professor Krasso
; Date: 10, February, 2024
; Modified by: Joanna Brumfield
; Description: Python Conditionals, Lists, and Loops
;===========================================
"""""

"Create a list of at least 5 hobbies."
myHobbies = ["Gardening", "Floral Design", "Bead Embroidery", "Sewing", "Cooking" , "Plant Propagation", "Hiking", "Mycology"]

"Use a for loop to iterate over the list of hobbies and print them to the console window."
for x in myHobbies:
    print(x)

"Create a list of days (Sunday through Saturday)."    
week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

"Use a for loop to iterate over the list of days and add an if…else statement to display what the day is.  For Saturday and Sunday display a message indicating you are off and should enjoy your hobbies.  For all other days display a message indicating it is a work day."
for x in week:
    print(x)
    if x == 'Sunday' or x == 'Saturday':
        print("Off work, enjoy your hobbies!")
    else: 
        print("Work Day :(")