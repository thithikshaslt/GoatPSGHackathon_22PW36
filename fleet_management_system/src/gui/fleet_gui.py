from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene
from PyQt5.QtCore import Qt
from ..models.nav_graph import NavGraph

class FleetGUI(QGraphicsView):
    def __init__(self, nav_graph: NavGraph):
        super().__init__()
        self.scene = QGraphicsScene()
        self.setScene(self.scene)
        self.nav_graph = nav_graph
        self.draw_graph()

    def draw_graph(self):
        # Draw vertices (circles) and lanes (lines)
        for vertex_id, vertex in self.nav_graph.vertices.items():
            x, y = vertex["x"], vertex["y"]
            self.scene.addEllipse(x, y, 10, 10)  # Adjust scaling as needed
        for lane in self.nav_graph.lanes:
            start = self.nav_graph.vertices[lane["start"]]
            end = self.nav_graph.vertices[lane["end"]]
            self.scene.addLine(start["x"], start["y"], end["x"], end["y"])