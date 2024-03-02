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

ca = certifi.where()
# Connection string
client = MongoClient("mongodb+srv://web335_admin:s3cret@whatabookdb.ff1ouoz.mongodb.net/whatABookDB?retryWrites=true&w=majority", tlsCAFile=ca)

# Variable to access whatABookDB
db = client['whatABookDB']

# # Write a query to display a list of books.
print("Complete Book List: ")
for books in db.books.find():
  print(books)

# Write a query to display a list of books by genre.
print("Genre Fiction: ")
for books in db.books.find({"genre": "Fiction"}):
  print(books)
  
# Write a query to display a list of book by author.
print("Author: Charles Dickens ")
for books in db.books.find({"author": "Charles Dickens"}):
  print(books)
  
# Write a query to display a book by bookId.
print("Book by ID: 65e23919fe0e7fb6b77bc569 ")
for book in db.books.find({"_id": ObjectId('65e23919fe0e7fb6b77bc569')}):
  print(book)