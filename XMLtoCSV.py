import xml.etree.ElementTree as ET
import csv

tree = ET.parse("JTX.xml")
root = tree.getroot()

f = open("XTC.csv", "w", newline="")

csvwriter = csv.writer(f)
head = ["phone_nr", "message"]
csvwriter.writerow(head)

for entry in root.findall("item"):
    row = []
    job_name = entry.find("phone_nr").text
    row.append(job_name)
    task_name = entry.find("message").text
    row.append(task_name)
    csvwriter.writerow(row)
f.close()


