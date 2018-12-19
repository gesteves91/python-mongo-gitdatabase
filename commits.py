import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["msr14"]
mycol = mydb["commits"]

myquery = { "sha": "fffcc4e85c3eae0b976f2f081c23bab21fd289d9" }

mydoc = mycol.find(myquery)
#mydoc = mycol.distinct("committer.id")
#cursor = mycol.find({})

#x = mycol.find_one()
#print(x)

for x in mydoc:
  print(x)
