import numpy as np
import copy

def choose_edge(G):
    #print("G", G)
    nodes = []
    edges = []
    [(nodes.append(node), edges.append(node_edges)) for node, node_edges in G.items()]
    edges_len_list = [len(node_edges) for node_edges in edges]
    #print(nodes, edges)

    v1 = np.random.choice(nodes, p = np.array(edges_len_list)/ sum(edges_len_list))
    #print(v1)
    v2 = np.random.choice(G[v1])
    #print(v1, G[v1])

    return v1, v2

def edge_contract(G):
    v1, v2 = choose_edge(G)
    #print(v1, v2)
    G[v1].extend(G[v2])
    G.pop(v2)

    for node, edges in G.items():
        G[node] = [v1 if i == v2 else i for i in edges]

    while v1 in G[v1]:
        G[v1].remove(v1)

    #print(v1, v2, G)

        #print(G[v1])

def count_cross(G):
    for node, edges in G.items():
        return len(edges)

def loop(G):
    while len(G) > 2:
        edge_contract(G)
    count = count_cross(G)
    return count

def min_cut(G):
    count = 1000000
    for i in range(100):
        #it's important to use deepcopy!
        G1 = copy.deepcopy(G)
        temp = loop(G1)
        if count > temp:
            count = temp
        print(count)
    return count

def build_gragh():
    G = {}
    with open('kargerMinCut.txt', 'r') as f:
        for i in range(200):
            line = list(map(int, f.readline().split()))
            #print(line)
            G[line[0]] = line[1:]

    return G


if __name__ == "__main__":
    '''
    min = 10000
    for i in range(1000):
        G = build_gragh()
        c = loop(G)

        if min > c:
            min = c
        print(min)
    '''

    #G = {1:[2,3], 2:[1,3], 3:[1,2]}
    #print(G)

    G = build_gragh()
    count = min_cut(G)
    print(count)


