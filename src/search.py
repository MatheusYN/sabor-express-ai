import time
from collections import deque
import heapq

# BFS
def bfs(grafo, inicio, destino):
    fila = deque([(inicio, [inicio])])
    visitados = set()
    while fila:
        no, caminho = fila.popleft()
        if no == destino:
            return caminho
        if no not in visitados:
            visitados.add(no)
            for vizinho, _ in grafo.vizinhos(no):
                fila.append((vizinho, caminho + [vizinho]))
    return None

# DFS
def dfs(grafo, inicio, destino, caminho=None, visitados=None):
    if caminho is None:
        caminho = [inicio]
    if visitados is None:
        visitados = set()
    if inicio == destino:
        return caminho
    visitados.add(inicio)
    for vizinho, _ in grafo.vizinhos(inicio):
        if vizinho not in visitados:
            novo_caminho = dfs(grafo, vizinho, destino, caminho + [vizinho], visitados)
            if novo_caminho:
                return novo_caminho
    return None

# A*
def heuristica(no, destino):
    return abs(hash(no) - hash(destino)) % 10

def a_star(grafo, inicio, destino):
    fila = [(0, inicio, [inicio])]
    visitados = set()
    while fila:
        custo, no, caminho = heapq.heappop(fila)
        if no == destino:
            return caminho
        if no not in visitados:
            visitados.add(no)
            for vizinho, peso in grafo.vizinhos(no):
                prioridade = custo + peso + heuristica(vizinho, destino)
                heapq.heappush(fila, (prioridade, vizinho, caminho + [vizinho]))
    return None

# Função para medir tempo
def medir_tempo(funcao, grafo, inicio, destino):
    inicio_tempo = time.time()
    caminho = funcao(grafo, inicio, destino)
    fim_tempo = time.time()
    return caminho, fim_tempo - inicio_tempo

