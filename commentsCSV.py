import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["msr14"]
mycol = mydb["commit_comments"]

# Get all the unique commit ids.
mydoc = mycol.find({}, {'body': 1})

for x in mydoc:
    if x['body'] is not None:
        print(x['body'])