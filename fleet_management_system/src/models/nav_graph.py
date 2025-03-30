import json
import networkx as nx

class NavigationGraph:
    def __init__(self, file_path):
        with open(file_path, "r") as f:
            data = json.load(f)
        
        self.graph = nx.Graph()
        self.vertices = data["levels"]["level1"]["vertices"]
        self.lanes = data["levels"]["level1"]["lanes"]

        for i, vertex in enumerate(self.vertices):
            self.graph.add_node(i, pos=(vertex[0], vertex[1]), **vertex[2])
        
        for lane in self.lanes:
            self.graph.add_edge(lane[0], lane[1], **lane[2])
    
    def get_position(self, node):
        return self.graph.nodes[node]["pos"]

    def find_shortest_path(self, start, end):
        return nx.shortest_path(self.graph, source=start, target=end, weight="speed_limit")

