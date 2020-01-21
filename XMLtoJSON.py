import xmltodict
import json

with open("JTX.xml") as in_file:
    xml = in_file.read()
    with open("XTJ.json", "w") as out_file:
        json.dump(xmltodict.parse(xml), out_file)
