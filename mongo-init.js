use admin
db.createUser(
  {
    user: "admin",
    pwd: "test1234",
    roles: [ { role: "userAdminAnyDatabase", db: "admin" }, "readWriteAnyDatabase" ]
  }
)
db.status.insertOne({"text": "active"});