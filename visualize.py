import matplotlib.pyplot as plt
import networkx as nx

def draw_graph(graph, coords):
    G = nx.Graph()
    for u, neighbors in graph.items():
        for v, w in neighbors.items():
            G.add_edge(u, v, weight=w)

    plt.figure(figsize=(10, 7))
    nx.draw_networkx(G, coords, node_color='lightblue', node_size=700)
    nx.draw_networkx_edge_labels(G, coords,
        edge_labels=nx.get_edge_attributes(G, 'weight'))
    plt.title("Graph visualization")
    plt.axis('off')
    plt.show()
