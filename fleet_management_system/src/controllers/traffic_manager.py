from queue import Queue

class TrafficManager:
    def __init__(self):
        self.occupied_lanes = set()  # Stores (start, end) lane tuples

    def request_lane(self, start: int, end: int) -> bool:
        if (start, end) in self.occupied_lanes:
            return False
        self.occupied_lanes.add((start, end))
        return True

    def release_lane(self, start: int, end: int):
        self.occupied_lanes.discard((start, end))