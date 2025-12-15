import heapq

def dijkstra(graph, start, goal):
    pq = [(0, start)]
    dist = {n: float('inf') for n in graph}
    dist[start] = 0
    parent = {start: None}
    visited = set()
    pop_count = 0

    while pq:
        current_dist, u = heapq.heappop(pq)
        pop_count += 1

        if u in visited:
            continue
        visited.add(u)

        if u == goal:
            break

        for v, cost in graph[u].items():
            nd = current_dist + cost
            if nd < dist[v]:
                dist[v] = nd
                parent[v] = u
                heapq.heappush(pq, (nd, v))

    path = []
    node = goal
    while node:
        path.insert(0, node)
        node = parent.get(node)

    return path, dist[goal], visited, pop_count
