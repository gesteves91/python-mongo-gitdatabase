import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["msr14"]
mycol = mydb["commits_comments"]

myquery = { "commit_id": "cba2407f4a86c0a040fe0473615f9987ab108b9c" }

mydoc = mycol.find(myquery)

for x in mydoc:
  print(x)
