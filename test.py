import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["msr14"]
mycol = mydb["repos"]

myquery = { "name": "akka" }

mydoc = mycol.find(myquery)

for x in mydoc:
  print(x)
