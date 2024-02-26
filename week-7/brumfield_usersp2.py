"""""
============================================
; Title:  brumfield_usersp2.py 
; Author: Professor Krasso
; Date: 25, February, 2024
; Modified by: Joanna Brumfield
; Description: Python with MongoDB, Part 2
;===========================================
"""""

# Import Mongo
from pymongo import MongoClient
import datetime
import certifi

ca = certifi.where()
# Connection string
client = MongoClient("mongodb+srv://web335_user:s3cret@web335db.xempkut.mongodb.net/web335DB?retryWrites=true&w=majority&appName=web335DB", tlsCAFile=ca)

# Variable to access web335DB
db = client['web335DB']

# collection = db["users"]

#Write the Python code to create a new user document.
import datetime

record = {
    "firstName": "John",
    "lastName": "Doe",
    "employeeId": "9999",
    "email": "john1@me.com",
    "last_modified": datetime.datetime.now(tz=datetime.timezone.utc)
}
result = db.users.insert_one(record)
print(record)

#Write the Python code to display the newly created document.
search_user_name = db.users.find_one({"firstName": "John"})
print(search_user_name)

#Write the Python code to update the email address of the document you created in step 2.
new_email = db.users.update_one({"firstName": "John"},
                    {"$set": {"email": "doe123@me.com"}}
                    )
print(new_email)
#Write the Python code to display the updated document.
updated_document = db.users.find_one({"firstName": "John"})
print(updated_document)

#Write the Python code to delete the document you created in step 3.
db.users.delete_one({"firstName": "John", "email": "john1@me.com"})

#Write the Python code to prove the document was deleted.
deleted_user = db.users.find_one({"firstName": "John", "email": "john1@me.com"})
if deleted_user is None:
    print('user has succesfully been deleted')
else:
    print('user was not deleted')
    