class Vertex:
    def __init__(self, key, lon, lat):
        self.id = key
        self.lon = lon 
        self.lat = lat
        self.connected_to = {}
        
    def add_neighbor(self, nbr, weight=0):
        self.connected_to[nbr] = weight

    def get_connections(self):
        return self.connected_to.keys()

    def get_id(self):
        return self.id

    def get_weight(self, nbr):
        return self.connected_to[nbr]
