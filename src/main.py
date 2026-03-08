from src.graph import Grafo
from src.search import bfs, dfs, a_star, medir_tempo
from src.clustering import agrupar_entregas
import matplotlib.pyplot as plt
import networkx as nx

# Carregar grafo do CSV
grafo = Grafo.carregar_de_csv("data/mapa.csv")

# Medir tempos
caminho_bfs, tempo_bfs = medir_tempo(bfs, grafo, "A", "F")
caminho_dfs, tempo_dfs = medir_tempo(dfs, grafo, "A", "F")
caminho_astar, tempo_astar = medir_tempo(a_star, grafo, "A", "F")

print("BFS:", caminho_bfs, "Tempo:", tempo_bfs)
print("DFS:", caminho_dfs, "Tempo:", tempo_dfs)
print("A* :", caminho_astar, "Tempo:", tempo_astar)

# Gerar imagem do grafo
grafo.desenhar("docs/grafo.png")
print("Imagem do grafo salva em docs/grafo.png")

# Exemplo clustering
pontos = [(1,2), (2,3), (10,10), (11,11), (50,50)]
labels, centros = agrupar_entregas(pontos, k=2, caminho_saida="docs/clusters.png")
print("Clusters:", labels)
print("Centros:", centros)
print("Imagem dos clusters salva em docs/clusters.png")

# Gráfico comparativo dos tempos
plt.figure(figsize=(6,4))
algoritmos = ["BFS", "DFS", "A*"]
tempos = [tempo_bfs, tempo_dfs, tempo_astar]
plt.bar(algoritmos, tempos, color=["blue","green","orange"])
plt.title("Comparação de Tempo de Execução")
plt.ylabel("Tempo (segundos)")
plt.savefig("docs/comparacao_tempos.png")
plt.close()
print("Gráfico de comparação salvo em docs/comparacao_tempos.png")

# Exemplo de pontos e clusters
pontos = [(1,2), (2,3), (10,10), (11,11), (50,50)]
labels, centros = agrupar_entregas(pontos, k=2)

# Plotar clusters com rotas simples
plt.figure(figsize=(6,6))
for i, ponto in enumerate(pontos):
    plt.scatter(ponto[0], ponto[1], c="C"+str(labels[i]), s=100)
plt.scatter(centros[:,0], centros[:,1], c="red", marker="X", s=200, label="Centros")

# Exemplo de rota ligando pontos do cluster 0
cluster0 = [p for i,p in enumerate(pontos) if labels[i]==0]
if len(cluster0) > 1:
    xs, ys = zip(*cluster0)
    plt.plot(xs, ys, c="blue", linestyle="--", label="Rota Cluster 0")

# Exemplo de rota ligando pontos do cluster 1
cluster1 = [p for i,p in enumerate(pontos) if labels[i]==1]
if len(cluster1) > 1:
    xs, ys = zip(*cluster1)
    plt.plot(xs, ys, c="green", linestyle="--", label="Rota Cluster 1")

plt.title("Clusters + Rotas Otimizadas")
plt.legend()
plt.savefig("docs/clusters_rotas.png")
plt.close()
print("Imagem clusters + rotas salva em docs/clusters_rotas.png")

