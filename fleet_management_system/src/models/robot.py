class Robot:
    def __init__(self, robot_id, start_node):
        self.id = robot_id
        self.position = start_node
        self.path = []
        self.status = "Idle"

    def assign_task(self, path):
        self.path = path
        self.status = "Moving"

    def move(self):
        if self.path:
            self.position = self.path.pop(0)
            if not self.path:
                self.status = "Task Complete"
