import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["msr14"]
mycol = mydb["commit_comments"]

# Get all the unique commit ids.
mydoc = mycol.distinct("commit_id")

for x in mydoc:
  print(x)
