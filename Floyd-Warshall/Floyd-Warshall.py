import math

from DGraph import DGraph

def floydWarshall(graph):
    tamanho = graph.size
    matrix = [[[math.inf, _+1] for i in range(tamanho)] for _ in range(tamanho)]
    for i in range(tamanho):
        matrix[i][i] = [0, i+1]

    for edge in graph.getAllEdges():
        matrix[edge[0]-1][edge[1]-1][0] = edge[2]

    for i in range(tamanho):
        for j in range(tamanho):
            for k in range(tamanho):
                if(matrix[j][i][0] + matrix[i][k][0] < matrix[j][k][0]):
                    matrix[j][k][0] = matrix[j][i][0] + matrix[i][k][0]
                    matrix[j][k][1] = matrix[i][k][1]

    return matrix

g = DGraph(5)
g.addEdge(1, 2, 4)
g.addEdge(1, 3, 5)
g.addEdge(1, 4, 3)
g.addEdge(1, 5, 2)
g.addEdge(2, 1, 1)
g.addEdge(2, 3, 10)
g.addEdge(2, 4, 6)
g.addEdge(3, 1, 3)
g.addEdge(3, 2, 1)
g.addEdge(3, 4, 9)
g.addEdge(3, 5, 7)
g.addEdge(4, 1, 2)
g.addEdge(4, 3, 8)
g.addEdge(4, 5, 9)

m = floydWarshall(g)

for i in range(len(m)):
    print(m[i])