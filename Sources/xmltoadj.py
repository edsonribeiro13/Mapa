import sys
from gistfile1 import *

file_name = open("Sources\map.osm")

G = read_osm(file_name)
networkx.write_adjlist(G, "uesb.adjlist")

