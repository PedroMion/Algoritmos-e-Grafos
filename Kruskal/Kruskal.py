from Graph import Graph
from UnionFind import UnionByRank

def Kruskal(graph):
    mst = Graph(graph.size)
    uf = UnionByRank(graph.size)
    edgesInOrder = sorted(graph.getAllEdges(), key=lambda x: x[2])
    edgesAdded = 0


    for edge in edgesInOrder:
        parent1 = uf.find(edge[0])
        parent2 = uf.find(edge[1])
        if(parent1 == parent2):
            continue
        else:
            uf.union(edge[0], edge[1])
            mst.addEdge(edge[0], edge[1], edge[2])
            edgesAdded += 1
            if(edgesAdded == (graph.size-1)): break
    
    return mst