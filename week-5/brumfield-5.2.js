db.users.insertOne({
    "firstName": "Antonio",
    "lastName": "Vivaldi",
    "employeeId": "1245",
    "email": "aVivaldi@me.com",
    "dateCreated": new Date()
});

 
db.users.updateOne(
    { "_id" : ObjectId("65bd2944f2e20dd3a02383e8")},
    {   
        $set : {"email" : "mozart@me.com" } ,
        $currentDate: { lastModified: true }
    }
);

db.users.aggregate (
    { $match: {} },
    { $project: { _id: 0, firstName: 1, lastName: 1, email: 1 } }
) 




