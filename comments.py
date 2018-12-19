import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["msr14"]
mycol = mydb["commits_comments"]

myquery = { "id": "988176" }

mydoc = mycol.find(myquery)

for x in mydoc:
  print(x)
