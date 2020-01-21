import csv

f = open("BaseData.csv")
csv_f = csv.reader(f)
data = []

for row in csv_f:
    data.append(row)
f.close()

fns = data[0]


def convert_row(row):
    return """<{a}={b}>
    <{d}>{c}</{d}>
    </{a}>""" .format(b=row[0], c=row[1], a=fns[0], d=fns[1])


# print(data[1:])
print('\n'.join([convert_row(row) for row in data]))
with open("CTX.xml", "w") as f: f.write('\n'.join([convert_row(row) for row in data[1:]]))