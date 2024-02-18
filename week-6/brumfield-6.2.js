/*
============================================
; Title:  brumfield_6.2
; Author: Professor Krasso
; Date: 18, February, 2024
; Modified by: Joanna Brumfield
; Description: MongoDB Aggregate Queries
;===========================================
*/
// Write a query to show a list of documents in the houses collection.  Take a screenshot of the output and save it as an image.
db.houses.find()
// Write a query to show a list of documents in the student’s collection.  Take a screenshot of the output and save it as an image.
db.students.find()
// Write a query to add a document to the student’s collection.  Take a screenshot of the output and save it as an image.  Next, write a query to prove the document was added to the user’s collection.  Take a screenshot of the output and save it as an image. 
db.students.insertOne({
    "firstName": "Jane",
    "lastName": "Smith",
    "studentId": "g7845",
    "houseId": "h8547"
})
// Write a query to delete the document you created in step 4.  Take a screenshot of the output and save it as an image.  Next, write a query to prove the document was added to the user’s collection.  Take a screenshot of the output and save it as an image.
db.students.remove({
    _id: ObjectId('65d273d4d9b9b6335543770c')
})
// Write a query to show a list of students by house (hint: use the lookup operation).  Take a screenshot of the output and save it as an image. 
db.students.aggregate({
    $lookup: {
        from: "houses",
        localField: "houseId",
        foreignField: "houseId",
        as: "studentsByHouse"
    }
})
//  Write a query to show a list of students for house Gryffindor (hint: use the lookup and match operations).  Take a screenshot of the output and save it as an image. 
db.students.aggregate([
    {
      $match: {
        "houseId": "h1007"
      }
    },
    {
      $lookup: {
        from: "houses",
        localField: "houseId",
        foreignField: "houseId",
        as: "studentsByGryffindor" 
      }
    }
  ])
  
// Write a query to show a list of students for the Eagle mascot (hint: use the lookup and match operations).  Take a screenshot of the output and save it as an image. 
db.students.aggregate([
    {
      $match: {
        "houseId": "h1009"
      }
    },
    {
      $lookup: {
        from: "houses",
        localField: "houseId",
        foreignField: "houseId",
        as: "EagleMascot" 
      }
    }
  ])