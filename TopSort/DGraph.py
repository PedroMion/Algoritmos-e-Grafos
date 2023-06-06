class DGraph():
    def __init__(self, size):
        self.size = size
        self.edges = [[] for _ in range(size)]
        self.inDeg = [0 for _ in range(size)]
        self.outDeg = [0 for _ in range(size)]
    
    def addEdge(self, origin, destiny):
        if(not(destiny in self.edges[origin])):
            self.edges[origin].append(destiny)
            self.inDeg[destiny] += 1
            self.outDeg[origin] += 1
    
    def addVertex(self):
        self.edges.append([])
        self.inDeg.append(0)
        self.outDeg.append(0)
    
    def removeEdge(self, origin, destiny):
        if((destiny in self.edges[origin])):
            self.edges[origin].remove(destiny)
            self.inDeg[destiny] -= 1
            self.outDeg[origin] -= 1

    def removeVertex(self, vertex):
        for neighbour in self.edges[vertex]:
            self.inDeg[neighbour] -= 1
        self.edges[vertex] = None
        self.inDeg[vertex] = None
        self.outDeg[vertex] = None
        for i in range(len(self.edges)):
            if (self.edges[i] != None and vertex in self.edges[i]):
                self.edges[i].remove(vertex)
                self.outDeg[i] -= 1

    def hasEdge(self, origin, destiny):
        if((destiny in self.edges[origin])): return True
        return False