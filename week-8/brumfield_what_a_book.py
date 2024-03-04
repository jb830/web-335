"""""
============================================
; Title:  brumfield_what_a_book.py 
; Author: Joanna Brumfield
; Date: 1, March, 2024
; Description: Pymongo scripts for WhatABook Project
;===========================================
"""""
# Import Mongo
from pymongo import MongoClient
import certifi
from bson import ObjectId
import json

ca = certifi.where()

# Connection string
client = MongoClient("mongodb+srv://web335_admin:s3cret@whatabookdb.ff1ouoz.mongodb.net/whatABookDB?retryWrites=true&w=majority", tlsCAFile=ca)

# Variable to access whatABookDB
db = client['whatABookDB']

# Display a list of books.
print("Complete Book List: ")
for books in db.books.find():
  print(json.dumps(books, indent=3, default=str))

# Display a list of books by genre.
print("Genre: ")
for books in db.books.find({"genre": "Fiction"}):
  print(json.dumps(books, indent=3, default=str))
  
# Display a list of book by author.
print("Author: Charles Dickens ")
for books in db.books.find({"author": "Charles Dickens"}):
  print(json.dumps(books, indent=3, default=str))
  
# Display a book by bookId.
print("Book by ID: 65e23919fe0e7fb6b77bc569 ")
for book in db.books.find({"_id": ObjectId('65e23919fe0e7fb6b77bc569')}):
  print(json.dumps(books, indent=3, default=str))

#Display a wishlist by customerIdAdd book to a customers wishlist
print("Wish List for: customer _id(65e23919fe0e7fb6b77bc581)")
for list in db.customers.find({"_id": ObjectId('65e23919fe0e7fb6b77bc581')},{ "wish_list"}):
  print(json.dumps(list, indent=3, default=str))
  
#Add a book from a customers wishlist & show wishlist for cutomer by Id
# book = ObjectId('65e23919fe0e7fb6b77bc560')
# customer = ObjectId('65e23919fe0e7fb6b77bc581')
# db.customer.update_one({customer}{"$push": {"wish_list": book}})

# print("Book added to: customer _id(65e23919fe0e7fb6b77bc581)")
# for list in db.customers.find({"_id": ObjectId('65e23919fe0e7fb6b77bc581')},{ "wish_list"}):
#   print(json.dumps(list, indent=3, default=str))

#Remove book from a customers wishlist
