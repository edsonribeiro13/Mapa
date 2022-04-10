import xml.etree.ElementTree as ET

file_name = "./map.osm"

tree = ET.parse(file_name)
root = tree.getroot()
file_name = file_name.replace('.xml', '.txt')
f=open(file_name, "w")
for node in root.iter('node'):
    ident = node.attrib['id']
    lat = node.attrib['lat']
    lon = node.attrib['lon']
    f.write("{} {} {}\n".format(ident,lat,lon))
f.close()