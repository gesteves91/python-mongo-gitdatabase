import csv
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["msr14"]
mycol = mydb["commits"]

cursor = mycol.find(
    {}, {'stats.deletions': 1, 'stats.additions': 1, 'stats.total': 1})

with open('commits.csv', 'w') as outfile:
    fields = ['stats.deletions', 'stats.additions', 'stats.total']
    write = csv.DictWriter(outfile, fieldnames=fields)
    write.writeheader()
    for commits in cursor:
        if 'stats' in commits:
            stats = commits['stats']
            print(stats)
            for key in stats:
                flattened_record = {
                'stats.deletions': stats[key],
                'stats.additions': stats[key],
                'stats.total': stats[key]
                }
                write.writerow(flattened_record)
    print("Writing complete!!!")