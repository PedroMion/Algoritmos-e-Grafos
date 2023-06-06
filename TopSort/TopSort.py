def topSort(graph):
    order = []
    queue = []
    for i in range(graph.size):
        if(graph.inDeg[i] == 0): queue.append(i)
    
    while(len(queue) != 0 and graph.size > len(order)):
        v = queue.pop()
        order.append(v)
        graph.removeVertex(v)
        for i in range(graph.size):
            if(graph.inDeg[i] == 0): queue.append(i)
    if(len(order) == graph.size): return order
    return None