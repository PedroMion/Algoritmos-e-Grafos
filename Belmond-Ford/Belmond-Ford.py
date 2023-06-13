from DGraph import DGraph
import math

def relaxEdge(edge, paths, previous):
    origin = edge[0]
    destiny = edge[1]
    cost = edge[2]
    change = False
    if((paths[origin] + cost) < paths[destiny]):
        paths[destiny] = paths[origin] + cost
        previous[destiny] = origin
        change = True
    return paths, previous, change


def belmondFord(graph, root):
    paths = [math.inf for _ in range(graph.size+1)]
    paths[root] = 0
    previous = [None for _ in range(graph.size+1)]

    for i in range(graph.size):
        somethingChanged = False
        everyEdge = graph.getAllEdges()
        for edge in everyEdge:
            paths, previous, change = relaxEdge(edge, paths, previous)
            if(change == True): somethingChanged = True
        if(not(somethingChanged)):
            break
    
    somethingChanged = False
    everyEdge = graph.getAllEdges()
    for edge in everyEdge:
        paths, previous, change = relaxEdge(edge, paths, previous)
        if(change == True): somethingChanged = True
    if(somethingChanged):
        return None
    return paths, previous

