import sys
from PyQt5.QtWidgets import QApplication
from models.nav_graph import NavGraph
from gui.fleet_gui import FleetGUI

def main():
    app = QApplication(sys.argv)
    nav_graph = NavGraph("data/nav_graph_1.json")
    gui = FleetGUI(nav_graph)
    gui.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()