import csv
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["msr14"]
mycol = mydb["commits"]

cursor = mycol.find(
    {}, {'stats.deletions': 1, 'stats.additions': 1, 'stats.total': 1})

with open('commits.csv', 'w') as outfile:
    fields = ['deletions', 'additions', 'total']
    write = csv.DictWriter(outfile, fieldnames=fields)
    write.writeheader()
    for commits in cursor:
        if 'stats' in commits:
            stats = commits['stats']
            #print(stats)
            count = 0
            for key in stats:
                if key == 'deletions':
                    deletions = stats[key]
                elif key == 'additions':
                    additions = stats[key]
                else:
                    total = stats[key]
            flattened_record = {
                'deletions': deletions,
                'additions': additions,
                'total': total
                }
            write.writerow(flattened_record)
            #print(count)
            #if count is not 3:
            #    print("Somethign is completely wrong!!!")
    print("Writing complete!!!")