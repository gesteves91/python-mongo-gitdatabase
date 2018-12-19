import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["msr14"]
mycol = mydb["commit_comments"]

count = 0

myquery = { "commit_id": 1 }

# Get all the unique commit ids.
#mydoc = mycol.distinct("commit_id")
mydoc = mycol.find({}, myquery)

for x in mydoc:
  #print(x)
  count = count + 1

print(count)
