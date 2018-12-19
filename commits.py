import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["msr14"]
mycol = mydb["commits"]

#myquery = { "_id": "52343e2ebd3543bb7f000002" }

#mydoc = mycol.find(myquery)
mydoc = mycol.distinct("committer.id")

for x in mydoc:
  print(x)
