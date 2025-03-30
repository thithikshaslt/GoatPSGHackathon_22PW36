class TrafficManager:
    def __init__(self):
        self.occupied_nodes = set()

    def can_move(self, robot):
        return robot.position not in self.occupied_nodes

    def update_position(self, robot):
        if self.can_move(robot):
            self.occupied_nodes.add(robot.position)
            robot.move()
            self.occupied_nodes.remove(robot.position)
