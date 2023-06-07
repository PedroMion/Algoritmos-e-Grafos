from BinaryHeap import BinaryHeap
from Graph import Graph

def primm(graph, root):
    heap = BinaryHeap()
    mst = Graph(graph.size)
    removeds = [root]
    current = graph.getEdgesByVertex(root)
    edgesAdded = 0

    for elem in current:
        heap.addElement(elem[0], elem[1], elem[2])

    while(heap.size > 0):
        edge = heap.getRoot()
        removeds.append(edge[0])
        mst.addEdge(edge[0], edge[1], edge[2])
        edgesAdded += 1

        if(edgesAdded == (graph.size - 1)): break

        current = graph.getEdgesByVertex(edge[0])
        for elem in current:
            if(not(elem[0] in removeds)):
                if(heap.isElementOnHeap(elem[0])):
                    heap.updateElement(elem[0], elem[1], elem[2])
                else: heap.addElement(elem[0], elem[1], elem[2])

    return mst