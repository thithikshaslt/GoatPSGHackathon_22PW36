import logging
import os

# Ensure logs directory exists
log_dir = os.path.join(os.path.dirname(__file__), "../logs")
os.makedirs(log_dir, exist_ok=True)

log_file = os.path.join(log_dir, "fleet_logs.txt")

# Configure logging
logging.basicConfig(filename=log_file, level=logging.INFO)

from models.robot import Robot

class FleetManager:
    def __init__(self):
        self.robots = {}

    def spawn_robot(self, robot_id, start_node):
        self.robots[robot_id] = Robot(robot_id, start_node)
        logging.info(f"Robot {robot_id} spawned at node {start_node}")

    def assign_task(self, robot_id, path):
        if robot_id in self.robots:
            self.robots[robot_id].assign_task(path)
            logging.info(f"Robot {robot_id} assigned path: {path}")
