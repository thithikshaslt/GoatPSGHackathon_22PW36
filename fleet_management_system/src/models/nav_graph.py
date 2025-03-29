import json
from typing import Dict, List

class NavGraph:
    def __init__(self, filepath: str):
        with open(filepath, 'r') as f:
            self.data = json.load(f)
        self.vertices = self._parse_vertices()
        self.lanes = self._parse_lanes()

    def _parse_vertices(self) -> Dict[int, Dict]:
        vertices = {}
        level = next(iter(self.data["levels"]))  # Get first level (e.g., "level1")
        for idx, vertex in enumerate(self.data["levels"][level]["vertices"]):
            vertices[idx] = {
                "x": vertex[0],
                "y": vertex[1],
                "name": vertex[2].get("name", ""),
                "is_charger": vertex[2].get("is_charger", False)
            }
        return vertices

    def _parse_lanes(self) -> List[Dict]:
        lanes = []
        level = next(iter(self.data["levels"]))
        for lane in self.data["levels"][level]["lanes"]:
            lanes.append({
                "start": lane[0],
                "end": lane[1],
                "speed_limit": lane[2].get("speed_limit", 0)
            })
        return lanes