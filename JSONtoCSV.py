import csv, json

f = open("CTJ.json", "r")
data = json.load(f)
f.close()

with open("JTC.csv", "w", newline="") as output:
    writer = csv.DictWriter(output, data[0].keys())
    writer.writeheader()
    writer.writerows(data)
    # for row in data:
    #     print(row)
    #     if row:
    #         writer.writerow(row)
