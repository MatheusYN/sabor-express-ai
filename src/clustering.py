
from sklearn.cluster import KMeans


def cluster_deliveries(locations, delivery_ids, n_clusters=3):
    if not delivery_ids:
        raise ValueError("Não existem entregas para agrupar.")

    if n_clusters < 1 or n_clusters > len(delivery_ids):
        raise ValueError(
            "O número de grupos deve estar entre 1 e o total de entregas."
        )

    coordinates = [
        [locations[node]["x"], locations[node]["y"]]
        for node in delivery_ids
    ]

    model = KMeans(
        n_clusters=n_clusters,
        random_state=42,
        n_init=10,
    )

    labels = model.fit_predict(coordinates)

    groups = {}

    for node, label in zip(delivery_ids, labels):
        group_name = int(label) + 1
        groups.setdefault(group_name, []).append(node)

    return groups