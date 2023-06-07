class Graph():
    def __init__(self, size):
        self.size = size
        self.edges = [[None for _ in range(size+1)] for _ in range(size+1)]
    
    def addEdge(self, v1, v2, weigth):
        if(v1 < v2 and v1 != v2):
            self.edges[v1][v2] = weigth
        elif(v2 < v1 and v1 != v2):
            self.edges[v2][v1] = weigth
    
    def removeEdge(self, v1, v2):
        if(v1 < v2 and v1 != v2):
            self.edges[v1][v2] = None
        elif(v2 < v1 and v1 != v2):
            self.edges[v2][v1] = None

    def getEdgesByVertex(self, vertex):
        list = []
        for i in range(len(self.edges)):
            if(self.edges[vertex][i] != None): list.append([i, vertex, self.edges[vertex][i]])
            elif(self.edges[i][vertex] != None): list.append([i, vertex, self.edges[i][vertex]])
        return list
    
    def getAllEdges(self):
        list = []
        for i in range(1,self.size+1):
            for j in range(1, self.size+1):
                if(self.edges[i][j] != None):
                    list.append([i, j, self.edges[i][j]])
        return list
