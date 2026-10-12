
import heapq


def dijkstra(graph, start, goal):
    if start not in graph or goal not in graph:
        raise ValueError("Origem ou destino inexistente.")

    queue = [(0, start)]
    distances = {node: float("inf") for node in graph}
    previous = {node: None for node in graph}
    distances[start] = 0

    while queue:
        current_distance, current = heapq.heappop(queue)

        if current_distance > distances[current]:
            continue

        if current == goal:
            break

        for neighbor, weight in graph[current].items():
            new_distance = current_distance + weight

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous[neighbor] = current
                heapq.heappush(queue, (new_distance, neighbor))

    if distances[goal] == float("inf"):
        return None, float("inf")

    path = []
    current = goal

    while current is not None:
        path.append(current)
        current = previous[current]

    path.reverse()
    return path, distances[goal]
