import math

from modules.genetics.chromossome import Chromossome

# Vertex i (row) is adjacent to vertex j (column), where graph[i][j] is the edge weight
# If the graph is not complete, a non adjacent vertex is defined by None
GRAPH = (
    (0, 2, 8, 5),
    (2, 0, 3, 4),
    (8, 3, 0, 7),
    (5, 3, 7, 0)
)

# Arbitrarily long edge to complete graph (if there are any non adjacent vertexes)
NON_ADJACENT_WEIGHT = 20


def f(chromossome):
    route = Chromossome.get_fenotype(chromossome.get_genes())

    total_weight = 0
    total_vertexes = len(GRAPH)

    for i in range(total_vertexes):
        vertex = route[i]
        next_vertex = route[i + 1]

        edge_weight = GRAPH[vertex][next_vertex]

        if edge_weight is None:
            edge_weight = NON_ADJACENT_WEIGHT

        total_weight += edge_weight

    return total_weight

# Fitness
def g(chromossome):
    return 1 / (1 + f(chromossome))

def f_average(population):
    avg = 0

    for chromossome in population:
        avg += f(chromossome)

    avg /= len(population)

    return avg

def g_average(population):
    avg = 0

    for chromossome in population:
        avg += g(chromossome)

    avg /= len(population)

    return avg