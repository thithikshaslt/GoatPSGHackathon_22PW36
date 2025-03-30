from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QGraphicsScene, QGraphicsView, QGraphicsEllipseItem
from PyQt6.QtGui import QPen, QBrush, QColor
from PyQt6.QtCore import Qt, QTimer
import sys
from models.nav_graph import NavigationGraph
from controllers.fleet_manager import FleetManager
from controllers.traffic_manager import TrafficManager

class FleetGUI(QMainWindow):
    def __init__(self, nav_graph):
        super().__init__()
        self.nav_graph = nav_graph
        self.fleet_manager = FleetManager()
        self.traffic_manager = TrafficManager()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Fleet Management System")
        self.setGeometry(100, 100, 800, 600)

        self.scene = QGraphicsScene()
        self.view = QGraphicsView(self.scene, self)
        self.view.setGeometry(50, 50, 700, 500)

        self.spawn_button = QPushButton("Spawn Robot", self)
        self.spawn_button.setGeometry(50, 560, 150, 30)
        self.spawn_button.clicked.connect(self.spawn_robot)

        self.robots = {}
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_simulation)
        self.timer.start(1000)

        self.draw_graph()

    def draw_graph(self):
        for node in self.nav_graph.graph.nodes:
            x, y = self.nav_graph.get_position(node)
            ellipse = QGraphicsEllipseItem(x * 50, y * 50, 10, 10)
            ellipse.setBrush(QBrush(QColor(0, 0, 255)))
            self.scene.addItem(ellipse)

    def spawn_robot(self):
        robot_id = len(self.robots)
        start_node = list(self.nav_graph.graph.nodes)[robot_id % len(self.nav_graph.graph.nodes)]
        self.fleet_manager.spawn_robot(robot_id, start_node)
        self.robots[robot_id] = self.nav_graph.get_position(start_node)

    def update_simulation(self):
        for robot_id, position in self.robots.items():
            robot = self.fleet_manager.robots.get(robot_id)
            if robot and robot.status == "Moving":
                self.traffic_manager.update_position(robot)
                self.robots[robot_id] = self.nav_graph.get_position(robot.position)
                self.scene.clear()
                self.draw_graph()
                self.update_robots()

    def update_robots(self):
        for pos in self.robots.values():
            ellipse = QGraphicsEllipseItem(pos[0] * 50, pos[1] * 50, 10, 10)
            ellipse.setBrush(QBrush(QColor(255, 0, 0)))
            self.scene.addItem(ellipse)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    nav_graph = NavigationGraph("data/nav_graph.json")
    gui = FleetGUI(nav_graph)
    gui.show()
    sys.exit(app.exec())
