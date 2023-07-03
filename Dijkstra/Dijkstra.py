import math

from Heap import BinaryHeap
from DGraph import DGraph

def dijkstra(root, graph):
    costs = [math.inf for _ in range(graph.size+1)]
    visiteds = [root]
    heap = BinaryHeap()
    current = root

    costs[0] = None
    costs[root] = 0

    while(len(visiteds) < graph.size):
        for edge in graph.getEdgesFromVertex(current):
            if(costs[current] + edge[1] < costs[edge[0]]):
                costs[edge[0]] = costs[current] + edge[1]
                heap.addElement(edge[0], edge[1])
        current = heap.getRoot()[0]
        visiteds.append(current)

    return costs

