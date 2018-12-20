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
    for field in cursor:
        id = field['_id']
        for commits in field['commit']:
            flattened_record = {
                '_id': id,
                'commit.message': commits['message']
            }
            write.writerow(flattened_record)