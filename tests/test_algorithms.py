
import sys
import unittest
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR / "src"))

from graph import load_graph, load_locations, heuristic
from astar import astar
from dijkstra import dijkstra
from clustering import cluster_deliveries


class TestAlgorithms(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.locations = load_locations()
        cls.graph = load_graph()

    def test_astar_and_dijkstra_same_cost(self):
        start = "A"
        goal = "J"

        path_a, cost_a = astar(
            self.graph,
            start,
            goal,
            lambda current, target: heuristic(
                self.locations, current, target
            ),
        )

        path_d, cost_d = dijkstra(self.graph, start, goal)

        self.assertIsNotNone(path_a)
        self.assertIsNotNone(path_d)
        self.assertAlmostEqual(cost_a, cost_d, places=6)

    def test_route_starts_and_ends_correctly(self):
        path, cost = dijkstra(self.graph, "A", "J")

        self.assertEqual(path[0], "A")
        self.assertEqual(path[-1], "J")
        self.assertGreater(cost, 0)

    def test_kmeans_creates_three_groups(self):
        delivery_ids = ["B", "D", "F", "G", "H", "I", "J", "C", "E"]

        groups = cluster_deliveries(
            self.locations,
            delivery_ids,
            n_clusters=3,
        )

        self.assertEqual(len(groups), 3)
        self.assertEqual(
            sum(len(nodes) for nodes in groups.values()),
            len(delivery_ids),
        )


if __name__ == "__main__":
    unittest.main()