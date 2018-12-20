import csv
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["msr14"]
mycol = mydb["commits"]

cursor = mycol.find(
    {}, {'_id': 1, 'commit.message': 1})

with open('stack_039.csv', 'w') as outfile:
    fields = ['id', 'commit.message']
    write = csv.DictWriter(outfile, fieldnames=fields)
    write.writeheader()
    for commits in cursor:
        id = commits['_id']
        for commit in commits['commit']:
            flattened_record = {
                '_id': id,
                'commit.message': commit['message']
            }
            write.writerow(flattened_record)