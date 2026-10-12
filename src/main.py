
import csv

from graph import load_graph, load_locations, heuristic
from astar import astar
from dijkstra import dijkstra
from clustering import cluster_deliveries
from visualization import create_visualizations


def load_delivery_ids():
    delivery_ids = []

    with open(
        "data/deliveries.csv",
        encoding="utf-8-sig",
        newline="",
    ) as file:
        for row in csv.DictReader(file):
            delivery_ids.append(row["location_id"])

    return delivery_ids


def main():
    locations = load_locations()
    graph = load_graph()

    start = "A"
    goal = "J"

    path_a, distance_a = astar(
        graph,
        start,
        goal,
        lambda current, target: heuristic(
            locations, current, target
        ),
    )

    path_d, distance_d = dijkstra(graph, start, goal)

    print("=== SABOR EXPRESS AI ===")
    print(f"Origem: {locations[start]['name']}")
    print(f"Destino: {locations[goal]['name']}")

    print("\n--- Algoritmo A* ---")
    print("Rota:", " -> ".join(path_a))
    print(f"Distância: {distance_a:.3f} km")

    print("\n--- Algoritmo Dijkstra ---")
    print("Rota:", " -> ".join(path_d))
    print(f"Distância: {distance_d:.3f} km")

    if abs(distance_a - distance_d) < 1e-9:
        print("\nValidação: os algoritmos encontraram o mesmo custo.")
    else:
        print("\nAtenção: os custos encontrados são diferentes.")

    delivery_ids = load_delivery_ids()
    groups = cluster_deliveries(
        locations,
        delivery_ids,
        n_clusters=3,
    )

    print("\n--- Agrupamento de entregas com K-Means ---")

    for group, nodes in sorted(groups.items()):
        print(f"\nGrupo {group}:")
        for node in nodes:
            print(f" - {node}: {locations[node]['name']}")

    create_visualizations(locations, graph, path_a, groups)


if __name__ == "__main__":
    main()