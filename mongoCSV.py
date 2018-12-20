import csv
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["msr14"]
mycol = mydb["commit_comments"]

cursor = mycol.find(
    {}, {'id': 1, 'commit_id': 1, 'body': 1})

with open('stack.csv', 'w') as outfile:
    fields = ['id', 'commit_id', 'body']
    write = csv.DictWriter(outfile, fieldnames=fields)
    write.writeheader()
    for commits in cursor:
        flattened_record = {
            'id': commits['id'],
            'commit_id': commits['commit_id'],
            'body': commits['body'],
        }
        write.writerow(flattened_record)