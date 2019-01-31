import network as nx
from network.readwrite import json_graph

class Loader():
    """
    Class to load the graph from different formats.
    
    Returns:
    --------
        A Nx graph object. 
    """

    def __init__(self):
        pass
    
    def from_dot(self, in_file):
        """
        Reading from dot file.
        Notes: (Too slow!)
        """          
        start = time.time()
        g = nx.drawing.nx_pydot.read_dot(in_file)
        end = time.time()
        print("Time taken for graph formation", end - start)
        return g

    def from_json(self, in_file):
        """
        Reading from json file.    
        """
        start = time.time()
        with open(in_file, 'r') as f:        
            json_graph = json.load(f)
            g = json_graph.node_link_graph(json_graph)
        end = time.time()    
        print("Time taken for graph formation", end - start)
        return g


    def from_graphML(self, in_file):
        """
        Reading from graphml file.    
        """
        pass

    
    def from_gxl(self, in_file):
        pass
