def DFS_directed_recur(G, s, current_order, nodes_explored, nodes_order):
    #Breadths first search for finding all the nodes connected to s undirected graph, also compute the distance to the s.
    #G: the undirected graph, nodes form 1 to N
    #s: the starting node
    #current_order: a list contianing a number to be changed every recursion
    nodes_explored.add(s)
    for edges in G:
        if edges[0] == s and edges[1] not in nodes_explored:
            DFS_directed_recur(G, edges[1], current_order, nodes_explored, nodes_order)
    nodes_order[s] = current_order[0]
    current_order[0] -= 1


def topo_order(G, N):
    nodes_explored = set()
    nodes_order = {}
    current_order = [N]
    for i in range(1, N + 1):
        if i not in nodes_order:
            DFS_directed_recur(G, i, current_order, nodes_explored, nodes_order)
            #nodes_order.update(nodes_order_new)
            #nodes_explored.update(nodes_order_new)

    return nodes_order

if __name__ == "__main__":
    #G = [[1,2], [2, 3], [1,3]]
    G = [[1,2], [2,3], [3, 4], [6, 4], [3,6], [2, 5], [1, 5], [5, 6]]

    #nodes_order = topo_order(G, 6)
    #print(nodes_order)

    nodes_exp = set()
    DFS_directed_recur(G, 1, [6], nodes_exp, {})

    order = topo_order(G, 6)





