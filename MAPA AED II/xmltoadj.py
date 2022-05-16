from gistfile1 import *

file_name = "./map.osm"
file_name = open(file_name, encoding = 'utf-8')

G = read_osm(file_name)
networkx.write_adjlist(G, "uesb.adjlist")

'''
Para que ocódigo funcione é necessário inserir essa função no digraph local

    def add_path(self, nodes, **attr):
        """Add a path.

        Parameters
        ----------
        nodes : iterable container
            A container of nodes.  A path will be constructed from
            the nodes (in order) and added to the graph.
        attr : keyword arguments, optional (default= no attributes)
            Attributes to add to every edge in path.

        See Also
        --------
        add_star, add_cycle

        Examples
        --------
        >>> G=nx.Graph()   # or DiGraph, MultiGraph, MultiDiGraph, etc
        >>> G.add_path([0,1,2,3])
        >>> G.add_path([10,11,12],weight=7)

        """
        nlist = list(nodes)
        edges = zip(nlist[:-1], nlist[1:])
        self.add_edges_from(edges, **attr)'''