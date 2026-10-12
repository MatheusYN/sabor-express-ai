
import heapq


def astar(graph, start, goal, heuristic):
    if start not in graph or goal not in graph:
        raise ValueError("Origem ou destino inexistente.")

    queue = [(heuristic(start, goal), 0, start)]
    came_from = {start: None}
    cost_so_far = {start: 0}

    while queue:
        _, current_cost, current = heapq.heappop(queue)

        if current_cost > cost_so_far[current]:
            continue

        if current == goal:
            break

        for neighbor, distance in graph[current].items():
            new_cost = current_cost + distance

            if (
                neighbor not in cost_so_far
                or new_cost < cost_so_far[neighbor]
            ):
                cost_so_far[neighbor] = new_cost
                came_from[neighbor] = current

                priority = new_cost + heuristic(neighbor, goal)
                heapq.heappush(
                    queue, (priority, new_cost, neighbor)
                )

    if goal not in came_from:
        return None, float("inf")

    path = []
    current = goal

    while current is not None:
        path.append(current)
        current = came_from[current]

    path.reverse()
    return path, cost_so_far[goal]