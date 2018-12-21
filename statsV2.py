import csv
import pymongo
import codecs

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["msr14"]
mycol = mydb["commits"]

cursor = mycol.find(
    {}, {'sha': 1, 'commit.message': 1, 'commit.comment_count': 1, 
         'stats.deletions': 1, 'stats.additions': 1, 'stats.total': 1})

with open('total.csv', 'w') as outfile:
    fields = ['sha', 'message', 'comment_count', 'deletions', 'additions', 'total']
    write = csv.DictWriter(outfile, fieldnames=fields)
    write.writeheader()
    for commits in cursor:
        sha = commits['sha']
        if 'commit' in commits:
            commit = commits['commit']
            for key in commit:
                message = commit['message'].encode('utf-8')
                comment_count = commit['comment_count']
        # Taking care of stats.
        if 'stats' in commits:
            stats = commits['stats']
            for key in stats:
                if key == 'deletions':
                    deletions = stats[key]
                elif key == 'additions':
                    additions = stats[key]
                else:
                    total = stats[key]
            flattened_record = {
                'sha': sha,
                'message': message,
                'comment_count': comment_count,
                'deletions': deletions,
                'additions': additions,
                'total': total
                }
            write.writerow(flattened_record)
    print("Writing complete!!!")