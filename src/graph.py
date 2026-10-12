
import csv
import math
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT_DIR / "data"


def load_locations():
    locations = {}

    with (DATA_DIR / "locations.csv").open(
        encoding="utf-8", newline=""
    ) as file:
        for row in csv.DictReader(file):
            locations[row["id"]] = {
                "name": row["name"],
                "x": float(row["x"]),
                "y": float(row["y"]),
            }

    return locations


def load_graph():
    graph = {node: {} for node in load_locations()}

    with (DATA_DIR / "roads.csv").open(
        encoding="utf-8", newline=""
    ) as file:
        for row in csv.DictReader(file):
            origin = row["origin"]
            destination = row["destination"]
            distance = float(row["distance"])

            if distance <= 0:
                raise ValueError("As distâncias devem ser positivas.")

            if origin not in graph or destination not in graph:
                raise ValueError("A rua contém um local desconhecido.")

            graph[origin][destination] = distance
            graph[destination][origin] = distance

    return graph


def heuristic(locations, current, goal):
    a = locations[current]
    b = locations[goal]

    return math.hypot(a["x"] - b["x"], a["y"] - b["y"])