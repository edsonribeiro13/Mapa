from asyncio.windows_events import NULL
from queue import Queue
from collections import defaultdict
from vertex import Vertex
from haversine import haversine
import popup

verticeN = open("map.osm", encoding = 'cp1252')
grafoN =  open("uesb.adjlist")

class Graph:
    def __init__(self):
        self.vert_list = {}

    def add_vertex(self, key, lat, lon):
        novo_vertice = Vertex(key, lat, lon)
        self.vert_list[key] = novo_vertice
        return novo_vertice
        
    def get_vertex(self, key):
        return self.vert_list[key]
        
    def add_edge (self, de, para):
        de = self.vert_list[de]
        para = self.vert_list[para]
        auxDe = Vertex.get_lat_lon(de)
        auxPara = Vertex.get_lat_lon(para)
        peso = haversine(auxDe,auxPara)
        Vertex.add_neighbor(de, para, peso)

    def get_vertices(self):
        return self.vert_list.keys()
        
    def get_edges(self):
        edges = set()
        for key, vertex in self.vert_list.items():
            for vizinho in vertex.connected_to:
                edges.add((key, vizinho.id, vertex.get_weight(vizinho)))
        return list(edges)

    def dijkstra(self, start, maxD=1e309):
         # total distance from origin
        tdist = defaultdict(lambda: 1e309)
        tdist[start] = 0
        # neighbour that is nearest to the origin
        preceding_node = {}
        unvisited = set(self.get_vertices())
        while unvisited:
            current = unvisited.intersection(tdist.keys())
            if not current: break
            min_node = min(current, key=tdist.get)
            unvisited.remove(min_node)
            vertex = self.get_vertex(min_node)
            #print (Vertex.get_connections(vertex))
            for neighbour in vertex.get_connections():
                d = tdist[min_node] + vertex.get_weight(neighbour)
                if tdist[neighbour.id] > d and maxD >= d:
                    tdist[neighbour.id] = d
                    preceding_node[neighbour.id] = min_node
        return tdist, preceding_node
    
    def min_path(self, start, end, maxD=1e309):
        tdist, preceding_node = self.dijkstra(start, maxD)
        dist = tdist[end]
        backpath = [end]
        try:
            while end != start:
                end = preceding_node[end]
                backpath.append(end)
            path = list(reversed(backpath))
        except KeyError:
            popup.msgErro()
            path = None
        return dist, path
   
g = Graph()
for i in verticeN:
    aux = i.split(" ")
    aux[1] = float(aux[1])
    aux[2] = aux[2].strip('\n')
    aux[2] = float(aux[2])
    g.add_vertex(key = aux[0], lat = aux[1], lon = aux[2])

for j in grafoN:
    if(j[0] != '#'):
        k = int(1)
        aux = j.split(" ")
        l = len(aux)
        l -= 1
        aux[l] = aux[l].strip('\n')
        while(l >= k):
            g.add_edge(aux[0], aux[k])
            k += 1
    
    