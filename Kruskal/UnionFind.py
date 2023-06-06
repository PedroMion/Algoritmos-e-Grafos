class UnionByRank():
    def __init__(self, size):
        self.size = size
        self.parents = [i for i in range(size+1)]
        self.ranks = [0 for _ in range(size+1)]
    
    def find(self, node):
        if(self.parents[node] == node):
            return node
        else:
            self.parents[node] = self.find(self.parents[node])
            return self.parents[node]
    
    def union(self, n1, n2):
        leader1 = self.find(n1)
        leader2 = self.find(n2)

        if(self.ranks[leader1] > self.ranks[leader2]):
            self.parents[leader2] = leader1
        elif(self.ranks[leader2] > self.ranks[leader1]):
            self.parents[leader1] = leader2
        else:
            self.parents[leader2] = leader1
            self.ranks[leader1] += 1
