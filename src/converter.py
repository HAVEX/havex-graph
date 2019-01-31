import network as nx
from networkx.readwrite import json_graph
import json

class Convertor():
    """
    Class containting methods to convert from different formats
    """
    def __init__(self):
        pass
        
    def dot_to_json(self, in_file, out_file):
        """
        Dot format to D3-JSON format. 
        """
        # Read into NetworkX using read_dot method
        graph_netx = nx.drawing.nx_pydot.read_dot(in_file)
        # Convert into json format ({ nodes: [], edges: [] })
        graph_json = json_graph.node_link_data(graph_netx)
        # write into outfile
        with open(outfile, 'w') as f:
            json.dump(graph_json, f, ensure_ascii=False)

    
    
