import networkx as nx

class Writer():
    """
    Methods to write the Graph in different formats.
    
    Args:
    -----
       The input graph (Nx format).

    Returns:
    -------
       Writes to the out_file (Output file).
    """
    def __init__(self, g):
        self.g = g

    def edge_list(self, out_file):
        self.edgeList = nx.write_edgelist(self.g, out_file)

    """
    Write adjacency matrix as a numpy file.
    """
    def adjacency_matrix(self, out_file):
        self.adjacencyMatrix = nx.to_numpy_matrix(self.g)
        np.save(out_file, self.adjacencyMatrix)

    """
    Writes the node array into numpy file.
    """        
    def nodes(self, out_file):
        pass
