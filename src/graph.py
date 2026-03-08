import csv
import networkx as nx
import matplotlib.pyplot as plt

class Grafo:
    def __init__(self):
        self.adjacencia = {}

    def adicionar_aresta(self, origem, destino, peso):
        if origem not in self.adjacencia:
            self.adjacencia[origem] = []
        if destino not in self.adjacencia:
            self.adjacencia[destino] = []
        self.adjacencia[origem].append((destino, peso))
        self.adjacencia[destino].append((origem, peso))  # grafo não-direcionado

    def vizinhos(self, no):
        return self.adjacencia.get(no, [])

    @staticmethod
    def carregar_de_csv(caminho_csv):
        grafo = Grafo()
        with open(caminho_csv, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for linha in reader:
                origem = linha['origem']
                destino = linha['destino']
                peso = float(linha['distancia'])
                grafo.adicionar_aresta(origem, destino, peso)
        return grafo

    def desenhar(self, caminho_saida="docs/grafo.png"):
        G = nx.Graph()
        for origem, vizinhos in self.adjacencia.items():
            for destino, peso in vizinhos:
                G.add_edge(origem, destino, weight=peso)

        pos = nx.spring_layout(G, seed=42)  # layout automático
        plt.figure(figsize=(6,6))
        nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=1500, font_size=12)
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.title("Mapa da Cidade - Grafo de Entregas")
        plt.savefig(caminho_saida)
        plt.close()