import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["msr14"]
mycol = mydb["commits_comments"]

mydoc = mycol.distinct("commit_id")

#mydoc = mycol.find(myquery)

for x in mydoc:
  print(x)
