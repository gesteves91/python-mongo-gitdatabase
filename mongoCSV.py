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
    for commits in cursor:  # Here we are using 'cursor' as an iterator
        id = commits['id']
        sha = commits['commit_id']
        body = commits['body']
        #for answer_record in answers_record['answers']:
        flattened_record = {
            'id': id,
            'commit_id': sha,
            'body': body,
        }
        write.writerow(flattened_record)