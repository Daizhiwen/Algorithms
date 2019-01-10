import copy
import sys

def DFS_directed_recur(G, s, nodes_explored, t, f, leader, current_leader):
    #Breadths first search for finding all the nodes connected to s undirected graph, also compute the distance to the s.
    #G: the undirected graph, nodes form 1 to N
    #s: the starting node
    #current_order: a list contianing a number to be changed every recursion
    nodes_explored.add(s)
    leader[s] = current_leader
    for edges in G:
        if edges[0] == s and edges[1] not in nodes_explored:
            DFS_directed_recur(G, edges[1], nodes_explored, t, f, leader, current_leader)
    t[0] += 1
    f[s] = t[0]

    #nodes_order[s] = current_order[0]
    #current_order[0] -= 1


def DFS_directed_iter(G, s, nodes_explored, t, f, leader, current_leader):
    #Breadths first search for finding all the nodes connected to s undirected graph, also compute the distance to the s.
    #G: the undirected graph, nodes form 1 to N
    #s: the starting node
    Q = [s]

    #{1: 1, 5: 2, 2: 3, 3: 4, 6: 5, 7: 6, 8: 7, 9: 8, 4: 9}
    while len(Q) > 0:
        v = Q.pop(0)
        t[0] -= 1
        f[v] = t[0]
        leader[v] = current_leader
        nodes_explored.add(v)
        print(nodes_explored)

        for edge in G:
            #initialize w
            w = -1
            if v == edge[0]:
                w = edge[1]
            #print(v, w)

            if w > 0 and w not in nodes_explored and w not in Q:
                #nodes_explored.add(w)
                Q.insert(0, w)


def DFS_loop(G, N, f = {}):
    nodes_explored = set()
    leader = {}
    t = [N + 1]
    s = None

    if len(f) > 0:
        l = list(f.items())
        l.sort(key=lambda x: x[1], reverse=True)

        for item in l:
            i = item[0]
            if i not in nodes_explored:
                s = i
                DFS_directed_iter(G, s, nodes_explored, t, f, leader, s)
    else:
        for i in range(N, 0, -1):
            if i not in nodes_explored:
                s = i
                DFS_directed_iter(G, s, nodes_explored, t, f, leader, s)
    return leader, f


def reverse_graph(G):
    G_c = copy.deepcopy(G)
    for edge in G_c:
        edge[0], edge[1] = edge[1], edge[0]
    return G_c

def count_scc(leader):
    scc = {}
    for key, value in leader.items():
        if value not in scc:
            scc[value] = 1
        else:
            scc[value] += 1

    l = list(scc.items())
    l.sort(key=lambda x: x[1], reverse=True)
    return l[0: 5]


if __name__ == "__main__":

    G = [[2, 1], [2, 3], [3, 2], [3, 4], [6, 4], [3, 6], [5, 2], [1, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 7]]
    G_rev = reverse_graph(G)
    leader, f = DFS_loop(G_rev, 9)
    print(f)
    print(leader)

    leader, f = DFS_loop(G, 9, f)
    print(leader)
    l = count_scc(leader)
    print(l)


    leader = {}
    DFS_directed_iter(G, 2, set(), f={}, t = [0], leader = leader, current_leader=1)

    print(leader)

    '''
    sys.setrecursionlimit(1000000)

    G = []
    with open('SCC.txt', 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            l = list(map(int, line.split()))
            G.append(l)

    G_rev = reverse_graph(G)
    leader, f = DFS_loop(G_rev, 875714)
    leader, f = DFS_loop(G, 875714, f)
    l = count_scc(leader)
    print(l)
    '''
