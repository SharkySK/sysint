import csv
import json

f = open("BaseData.csv")
csv_f = csv.DictReader(f)
data = []

for row in csv_f:
    data.append(row)

with open("CTJ.json", "w") as f:f.write(json.dumps(data, indent=2))
# print(json.dumps(data, indent=2))

