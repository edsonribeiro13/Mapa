import xml.etree.ElementTree as ET
import os

file_name = open("Sources\map.osm")
tree = ET.parse(file_name)
file_name.close
root = tree.getroot()
os.rename("Sources\map.osm", "Sources\map.txt")
file_name = open("Sources\map.txt")
f=open(file_name, "w")
for node in root.iter('node'):
    ident = node.attrib['id']
    lat = node.attrib['lat']
    lon = node.attrib['lon']
    f.write("{} {} {}\n".format(ident,lat,lon))
f.close()



