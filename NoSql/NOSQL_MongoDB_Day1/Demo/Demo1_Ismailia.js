use Clinic

//com1

//com2

use AI

use ai

//SELECT = FIND
//SQL SELECT * FROM inventory //Columns , WHERE

//MongoDB
db.inventory.find({})
//SQL SELECT _id, item  FROM inventory //Columns , WHERE
//db.inventory.find({ WHERE} , {Columns}  })
db.inventory.find({}, { _id: 1, item: 1 })

//SQL C 1 : C 15         C1 : C14
db.inventory.find({}, { _id: 0, item: 0 })

//SQL SELECT * FROM inventory WHERE quantity = 30

//MongoDB
db.inventory.find({quantity : 30})


//INSERT
//PK
db.empIsmaila.insertOne({name:"ahmed" ,age:20})  //Identity

db.empIsmaila.insertOne({name:"noha" ,age:20})  //Identity

db.empIsmaila.insertOne({name:"noha" ,age:20})  //Identity
 
db.empIsmaila.insertOne({_id:1,name:"eman" ,age:20}) //user defined

db.empIsmaila.find({})

ObjectId()

//UPDATE
//SQL UPDATE inventory SET age = 25 WHERE _id = 1

//MongoDB
//db.empIsmaila.updateOne({filter = WHERE } , {update})

db.empIsmaila.find({_id : 1})
db.empIsmaila.updateOne({_id : 1},{
    $set:{
        age : 25
    }
})

db.empIsmaila.find({name:"noha"})

//DELETE
db.empIsmaila.deleteMany({name:"noha"})
