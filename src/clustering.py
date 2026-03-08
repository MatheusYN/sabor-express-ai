import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def agrupar_entregas(pontos, k=3, caminho_saida="docs/clusters.png"):
    """
    pontos: lista de coordenadas [(x,y), (x,y)...]
    k: número de clusters
    """
    X = np.array(pontos)
    modelo = KMeans(n_clusters=k, random_state=42)
    modelo.fit(X)

    # Plotar clusters
    plt.figure(figsize=(6,6))
    plt.scatter(X[:,0], X[:,1], c=modelo.labels_, cmap="viridis", s=100)
    plt.scatter(modelo.cluster_centers_[:,0], modelo.cluster_centers_[:,1],
                c="red", marker="X", s=200, label="Centros")
    plt.title("Clusters de Entregas")
    plt.legend()
    plt.savefig(caminho_saida)
    plt.close()

    return modelo.labels_, modelo.cluster_centers_

