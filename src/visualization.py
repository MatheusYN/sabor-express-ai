from pathlib import Path

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import networkx as nx


ROOT_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = ROOT_DIR / "outputs"


def create_visualizations(locations, graph, route, groups):
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    positions = {
        node: (info["x"], info["y"])
        for node, info in locations.items()
    }

    network = nx.Graph()

    for node in graph:
        network.add_node(node)

    for origin, neighbors in graph.items():
        for destination, distance in neighbors.items():
            if not network.has_edge(origin, destination):
                network.add_edge(
                    origin, destination, weight=distance
                )

    # Grafico 1: rede e rota encontrada pelo A*
    plt.figure(figsize=(11, 6))

    nx.draw_networkx_edges(
        network, positions, edge_color="lightgray", width=1.5
    )
    nx.draw_networkx_nodes(
        network, positions, node_color="skyblue", node_size=900
    )
    nx.draw_networkx_labels(network, positions, font_size=10)

    route_edges = list(zip(route, route[1:]))

    nx.draw_networkx_edges(
        network,
        positions,
        edgelist=route_edges,
        edge_color="red",
        width=3,
    )

    nx.draw_networkx_nodes(
        network,
        positions,
        nodelist=route,
        node_color="orange",
        node_size=900,
    )

    nx.draw_networkx_labels(network, positions, font_size=10)

    plt.title("Sabor Express AI - Rota encontrada pelo A*")
    plt.xlabel("Coordenada X (simulada)")
    plt.ylabel("Coordenada Y (simulada)")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "rota_astar.png", dpi=200)
    plt.close()

    # Grafico 2: agrupamento das entregas com K-Means
    plt.figure(figsize=(11, 6))

    colors = ["royalblue", "darkorange", "seagreen"]

    for index, (group, nodes) in enumerate(sorted(groups.items())):
        xs = [locations[node]["x"] for node in nodes]
        ys = [locations[node]["y"] for node in nodes]

        plt.scatter(
            xs,
            ys,
            s=150,
            color=colors[index % len(colors)],
            label=f"Grupo {group}",
        )

        for node in nodes:
            plt.annotate(
                node,
                (locations[node]["x"], locations[node]["y"]),
                xytext=(5, 5),
                textcoords="offset points",
            )

    plt.scatter(
        [locations[node]["x"] for node in locations],
        [locations[node]["y"] for node in locations],
        s=20,
        color="gray",
        alpha=0.25,
        label="Todos os locais",
    )

    plt.title("Sabor Express AI - Agrupamento de entregas com K-Means")
    plt.xlabel("Coordenada X (simulada)")
    plt.ylabel("Coordenada Y (simulada)")
    plt.legend()
    plt.grid(alpha=0.2)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "grupos_kmeans.png", dpi=200)
    plt.close()

    print("\nGráficos salvos na pasta outputs:")
    print("- outputs/rota_astar.png")
    print("- outputs/grupos_kmeans.png")