import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["msr14"]
mycol = mydb["commits"]

myquery = { "": "Park Lane 38" }

mydoc = mycol.find(myquery)

for x in mydoc:
  print(x)
