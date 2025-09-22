use ITI_Mongo

// 2.	Create a Collection named "Staff".
// 3.	Insert one document into the "Staff" collection: {_id, name, age, gender, department}.

db.Staff.insertOne({
    _id: 1,
    name: "John ",
    age: 30,
    gender: "male",
    department: "HR"
});

//4.	Insert many documents into the "Staff" collection:
//•	   Object: {_id, name, age: 20, gender: "male", department}
//•	   Object: {_id, name, age: 25, gender: "female", managerName, department}
//•	   Object: {_id, name, age: 15, gender, DOB}

db.Staff.insertMany([

    { _id: 2, name: "Ahmed", age: 20, gender: "male", department: "Sales" },
    { _id: 3, name: "Sara", age: 25, gender: "female", managerName: "John", department: "Finance" },
    { _id: 4, name: "Ali", age: 15, gender: "male", DOB: "2010-05-10" }

]);

//5.	Query to find data from the "Staff" collection:
//•	1) Find all documents.

db.Staff.find({})

//•	2) Find documents where gender is "male".

db.Staff.findOne({ gender: "male" });

//•	3) Find documents with age between 20 and 25.
// $gt Greater Than
// $lt Less Than

db.Staff.find({
    $and: [
        { age: { $gte: 20 } },
        { age: { $lte: 25 } }
    ]
});

//•	4) Find documents where age is 25 and gender is "female".

db.Staff.findOne({ age: 25, gender: "female" })

//•	5) Find documents where age is 20 or gender is "female".

db.Staff.findOne({
    $or: [{ age: 20 }, { gender: "female" }]
});


// 6.	Update one document in the "Staff" collection where age is 15, set the name to "new student".

// Before  [ { "_id" : 4, "name" : "Ali", "age" : 15, "gender" : "male", "DOB" : "2010-05-10" } ]

db.Staff.updateOne(
    { age: 15 },
    { $set: { name: "new student" } }
);

//After : 
db.Staff.findOne({ age: 15 })
// 7.	Update many documents in the "Staff" collection, setting the department to "AI".
// Before : some have "HR", "Sales", "Finance", some have no department 

db.Staff.updateMany({},
    { $set: { department: "AI" } }
);

//After : 
db.Staff.find({})
// Now all departments are "AI"

//8.	Create a new collection called "test" and insert documents from Question 4.

db.createCollection("test");

db.test.insertMany([
    { _id: 5, name: "Ahmed", age: 20, gender: "male", department: "Sales" },
    { _id: 6, name: "Sara", age: 25, gender: "female", managerName: "John", department: "Finance" },
    { _id: 7, name: "Ali", age: 15, gender: "male", DOB: "2010-05-10" }
]);

db.test.find({})

//9.	Try to delete one document from the "test" collection where age is 15.

db.test.deleteOne({ age: 15 });

// 10. try to delete all male gender

// BEFORE:
db.test.find({ gender: "male" });

db.test.deleteMany({ gender: "male" });

//11.	Try to delete all documents in the "test" collection.

db.test.deleteMany({});
