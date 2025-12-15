import math
from graph_data import coords

def euclidean_heuristic(node, goal='G'):
    x1, y1 = coords[node]
    x2, y2 = coords[goal]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
