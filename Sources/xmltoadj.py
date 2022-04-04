import sys
from Sources.gistfile1 import *

G = read_osm(download_osm(-122.33,47.60,-122.31,47.61))
networkx.write_adjlist(G, "uesb.adjlist")

