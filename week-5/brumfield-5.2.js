/*
============================================
; Title:  brumfield_myworld.py 
; Author: Professor Krasso
; Date: 28, January, 2024
; Modified by: Joanna Brumfield
; Description: Pthon Math Functions
;===========================================
*/

//insert a new user to users collection 
db.users.insertOne({
    "firstName": "Antonio",
    "lastName": "Vivaldi",
    "employeeId": "1245",
    "email": "aVivaldi@me.com",
    "dateCreated": new Date()
});

//update email based on user _id 
db.users.updateOne(
    { "_id" : ObjectId("65bd2944f2e20dd3a02383e8")},
    {   
        $set : {"email" : "mozart@me.com" } ,
        $currentDate: { lastModified: true }
    }
);

//show only firstName, lastName, and email fields for all documents in users collection
db.users.aggregate (
    { $match: {} },
    { $project: { _id: 0, firstName: 1, lastName: 1, email: 1 } }
) 




