from gistfile1 import *

file_name = "./map.osm"
file_name = open(file_name)

G = read_osm(file_name)
networkx.write_adjlist(G, "./Sources/uesb.adjlist")