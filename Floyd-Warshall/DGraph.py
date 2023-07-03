class DGraph():
    def __init__(self, size):
        self.size = size
        self.edges = [[] for _ in range(size+1)]
    
    def addEdge(self, origin, destiny, weigth):
        for edge in self.edges[origin]:
            if(edge[0] == destiny):
                return
        self.edges[origin].append([destiny, weigth])

    def hasEdge(self, origin, destiny):
        if((destiny in self.edges[origin])): return True
        return False

    def getAllEdges(self):
        result = []
        for i in range(1, self.size+1):
            for edge in self.edges[i]:
                result.append([i, edge[0], edge[1]])
        return result