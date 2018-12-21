import csv
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["msr14"]
mycol = mydb["commits"]

cursor = mycol.find(
    {}, {'_id': 1, 'stats.total': 1, 'stats.additions': 1, 'stats.deletions': 1})

with open('commits.csv', 'w') as outfile:
    fields = ['id', 'stats.total', 'stats.additions', 'stats.deletions']
    write = csv.DictWriter(outfile, fieldnames=fields)
    write.writeheader()
    for commits in cursor:
        id = commits['_id']
        for stats in commits['stats']:
            print(type(stats))
            flattened_record = {
                '_id': id,
                'stats.total': stats['total'],
                'stats.additions': stats['additions'],
                'stats.deletions': stats['deletions']
            }
            write.writerow(flattened_record)