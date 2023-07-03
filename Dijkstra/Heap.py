class BinaryHeap():
    def __init__(self):
        self.heap = []
        self.size = 0
    
    def switch(self, i, j):
        temp = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = temp

    def moveUp(self, index):
        current = index
        parent = int((current - 1) / 2)

        while(parent >= 0):
            if(self.heap[current][1] < self.heap[parent][1]):
                self.switch(current, parent)
                current = parent
                parent = int((current - 1) / 2)
            elif(current <= 0 and parent <= 0):
                break
            else:
                break
        
    def isElementOnHeap(self, element):
        for elem in self.heap:
            if elem[0] == element: return True
        return False
    
    def addElement(self, vertex, weigth):
        if(self.isElementOnHeap(vertex)):
            self.updateElement(vertex, weigth)
            return
        self.heap.append([vertex , weigth])
        self.size += 1
        self.moveUp(len(self.heap)-1)

    def updateElement(self, vertex, weigth):
        for i in range(len(self.heap)):
            if(self.heap[i][0] == vertex):
                if(self.heap[i][1] < weigth): return
                self.heap[i] = [vertex, weigth]
                self.moveUp(i)

    def getRoot(self):
        root = self.heap[0]
        current = 0
        son1 = 1
        son2 = 2

        self.heap[0] = self.heap[len(self.heap)-1]
        self.heap.pop()

        while(son1 < len(self.heap) and son2 < len(self.heap)):
            if(self.heap[current][1] > self.heap[son1][1] and self.heap[current][1] > self.heap[son2][1]):
                minor = son1 if self.heap[son1][1] < self.heap[son2][1] else son2
                self.switch(minor, current)
                current = minor
                son1 = (current*2) + 1
                son2 = (current*2) + 2
            elif((self.heap[current][1] > self.heap[son1][1]) or (self.heap[current][1] > self.heap[son2][1])):
                minor = son1 if self.heap[son1][1] < self.heap[current][1] else son2
                self.switch(current, minor)
                current = minor
                son1 = (current*2) + 1
                son2 = (current*2) + 2
            else:
                break
        
        if(son1 < len(self.heap)):
            if(self.heap[current][1] > self.heap[son1][1]):
                self.switch(current, son1)

        self.size -= 1
        return root
