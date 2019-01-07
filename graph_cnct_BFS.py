def BFS_undirected(G, s):
    #Breadths first search for finding all the nodes connected to s undirected graph, also compute the distance to the s.
    #G: the undirected graph, nodes form 1 to N
    #s: the starting node
    Q = [s]
    nodes_explored = {s: 0}
    while len(Q) > 0:
        v = Q.pop(0)

        for edge in G:
            #initialize w
            w = -1
            if v == edge[0]:
                w = edge[1]
            elif v == edge[1]:
                w = edge[0]
            #print(v, w)

            if w > 0 and w not in nodes_explored:
                nodes_explored[w] = nodes_explored[v] + 1
                Q.append(w)
    return nodes_explored

def conected_class(G, N):
    node_classes = []
    nodes_exp = []
    for i in range(1, N + 1):
        if i not in nodes_exp:
            nodes_exp_new = BFS_undirected(G, i)
            nodes_exp.extend(list(nodes_exp_new.keys()))
            node_classes.append(list(nodes_exp_new.keys()))
    return node_classes


if __name__ == "__main__":
    G = [[1,2], [2, 3], [1,3]]

    nodes = BFS_undirected(G, 4)
    print(nodes)

    n = conected_class(G, 5)
    print(n)




