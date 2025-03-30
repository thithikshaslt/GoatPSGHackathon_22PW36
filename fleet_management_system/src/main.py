from PyQt6.QtWidgets import QApplication
import sys
from gui.fleet_gui import FleetGUI
from models.nav_graph import NavigationGraph

if __name__ == "__main__":
    app = QApplication(sys.argv)
    nav_graph = NavigationGraph("data/nav_graph_1.json")
    gui = FleetGUI(nav_graph)
    gui.show()
    sys.exit(app.exec())
