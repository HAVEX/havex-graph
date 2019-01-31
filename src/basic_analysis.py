import networkx as nx

class Analysis():

    def __init__(self, g):
        self.graph = g
    
    def info(self):
        print("Number of nodes {0}".format(len(self.graph.nodes())))
        print("Number of links {0}".format(len(self.graph.edges())))

    def find_root(self, node):
        if self.graph.predecessors(node):
            root = self.find_root(self.graph, self.graph.predecessors(node)[0])
        else:
            root = node
        return root
    
    def topological_ordering(self):
        print([n for n,d in self.graph.in_degree() if d==0])
        print(len(self.graph.nodes()))
        order = nx.topological_sort(self.graph)
        for o in order:
            print(o)
        return order
