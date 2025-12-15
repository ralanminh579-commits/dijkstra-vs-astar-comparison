from graph_data import graph, coords
from heuristics import euclidean_heuristic
from dijkstra import dijkstra
from astar import astar
from visualize import draw_graph

if __name__ == "__main__":
    draw_graph(graph, coords)

    path_d, cost_d, visited_d, pop_d = dijkstra(graph, 'S', 'G')
    path_a, cost_a, visited_a, pop_a = astar(
        graph, 'S', 'G', lambda n: euclidean_heuristic(n, 'G')
    )

    print("=== DIJKSTRA ===")
    print("Path:", path_d)
    print("Cost:", cost_d)
    print("Visited nodes:", visited_d)
    print("Pop operations:", pop_d)

    print("\n=== A* ===")
    print("Path:", path_a)
    print("Cost:", cost_a)
    print("Visited nodes:", visited_a)
    print("Pop operations:", pop_a)
