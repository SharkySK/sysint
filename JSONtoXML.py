import dicttoxml
import json
from xml.dom.minidom import parseString

f = open("CTJ.json", "r")
data = json.load(f)
f.close()

xml = dicttoxml.dicttoxml(data)

# dom = parseString(xml)
# print(dom.toprettyxml())

with open("JTX.xml", "wb") as f:
    f.write(xml)
