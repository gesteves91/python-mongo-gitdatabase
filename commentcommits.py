# Set the imports.
import csv
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["msr14"]
mycol = mydb["commit_comments"]

cursor = mycol.find(
  {}, {"commit_id": 1})

with open('commitComments.csv', 'w') as outfile:
    fields = ['deletions', 'additions', 'total']
    write = csv.DictWriter(outfile, fieldnames=fields)
    write.writeheader()
for commit_id in cursor:
  for key in commit_id:
    if key == 'commit_id':
      sha = commit_id[key]

      cursorCommit = mydb["commits"].find({"sha": sha})

      for commits in cursorCommit:
        print(commits)

