import heapq

def astar(graph, start, goal, heuristic):
    pq = [(heuristic(start), start)]
    g = {n: float('inf') for n in graph}
    g[start] = 0
    parent = {start: None}
    visited = set()
    pop_count = 0

    while pq:
        f, u = heapq.heappop(pq)
        pop_count += 1

        if u in visited:
            continue
        visited.add(u)

        if u == goal:
            break

        for v, cost in graph[u].items():
            ng = g[u] + cost
            if ng < g[v]:
                g[v] = ng
                parent[v] = u
                heapq.heappush(pq, (ng + heuristic(v), v))

    path = []
    node = goal
    while node:
        path.insert(0, node)
        node = parent.get(node)

    return path, g[goal], visited, pop_count
