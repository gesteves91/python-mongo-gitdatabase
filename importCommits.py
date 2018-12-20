import csv
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["msr14"]
mycol = mydb["commits"]

cursor = mycol.find(
    {}, {'id': 1, 'commit_id': 1, 'body': 1})

with open('stack_039.csv', 'w') as outfile:
    fields = ['commit.message']
    write = csv.DictWriter(outfile, fieldnames=fields)
    write.writeheader()
    for field in cursor:
        for commits in field['commit']:
            flattened_record = {
                'answers.message': commits['message']
            }
            write.writerow(flattened_record)