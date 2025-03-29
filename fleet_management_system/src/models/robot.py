from typing import Dict, List

class Robot:
    def __init__(self, robot_id: int, start_vertex: int):
        self.id = robot_id
        self.current_vertex = start_vertex
        self.destination = None
        self.path = []
        self.status = "idle"  # "moving", "waiting", "charging"

    def assign_task(self, destination: int, path: List[int]):
        self.destination = destination
        self.path = path
        self.status = "moving"

    def update_position(self):
        if self.status == "moving" and self.path:
            self.current_vertex = self.path.pop(0)
            if not self.path:
                self.status = "idle"