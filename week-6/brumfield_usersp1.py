"""""
============================================
; Title:  brumfield_usersp1.py 
; Author: Professor Krasso
; Date: 18, February, 2024
; Modified by: Joanna Brumfield
; Description: Python with MongoDB, Part 1
;===========================================
"""""

# Import Mongo
from pymongo import MongoClient

# Connection string
client = MongoClient("mongodb+srv://web335_user:s3cret@web335db.xempkut.mongodb.net/web335DB?retryWrites=true&w=majority")

# Variable to access web335DB
db = client['web335DB']

"Write the Python code to display all documents in the user’s collection."
for user in db.users.find():
    print(user)
# "Write the Python code to display a document where the employeeId is 1011."
for user in db.users.find({"employeeId": "1011"}):
    print(user)
"Write the Python code to display a document where the lastName is Mozart."
for user in db.users.find({"lastName": "Mozart"}):
    print(user)