db = db.getSiblingDB("labo01_db");
db.createCollection("users");

db.users.insertOne({name: "Admin",email: "admin@admin.com"});
db.users.insertOne({name: "John wick",email: "John@wick.com"});
db.users.insertOne({name: "Jane Doe",email: "Jame@Doe.com"});