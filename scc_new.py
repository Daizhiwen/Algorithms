import copy
import sys

def DFS_directed_recur(G, s, nodes_explored, t, f, leader, current_leader):
    #Breadths first search for finding all the nodes connected to s undirected graph, also compute the distance to the s.
    #G: the undirected graph, nodes form 1 to N
    #s: the starting node
    #current_order: a list contianing a number to be changed every recursion
    nodes_explored.add(s)
    leader[s] = current_leader
    #print(G[s])
    for edge in G[s]:
        if edge not in nodes_explored:
            DFS_directed_recur(G, edge, nodes_explored, t, f, leader, current_leader)
    t[0] += 1
    f[s] = t[0]

    #nodes_order[s] = current_order[0]
    #current_order[0] -= 1


def DFS_directed_iter(G, s, nodes_explored, t, f, leader, current_leader):
    #Breadths first search for finding all the nodes connected to s undirected graph, also compute the distance to the s.
    #G: the undirected graph, nodes form 1 to N
    #s: the starting node
    Q = [s]
    nodes_explored.add(s)
    leader[s] = current_leader
    #{1: 1, 5: 2, 2: 3, 3: 4, 6: 5, 7: 6, 8: 7, 9: 8, 4: 9}
    while len(Q) > 0:

        s = Q[-1]

        if len(G[s]) == 0 or belong(G[s], nodes_explored) == True:
            t[0] += 1
            f[s] = t[0]
            Q.pop()
        else:
            for v in G[s]:
                if v not in nodes_explored:
                    nodes_explored.add(v)
                    leader[v] = current_leader
                    Q.append(v)
                    break

def belong(l, p):
    for i in l:
        if i not in p:
            return False
    return True


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

def G_dict(G, N):
    G_d = dict()
    for edge in G:
        s = edge[0]
        v = edge[1]
        if s in G_d:
            G_d[s].add(v)
        else:
            G_d[s] = {v}
    for i in range(1, N + 1):
        if i not in G_d:
            G_d[i] = set()
    return G_d

if __name__ == "__main__":

    '''
    #G = [[2, 1], [2, 3], [3, 2], [3, 4], [6, 4], [3, 6], [5, 2], [1, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 7]]
    G = [[1,2], [2,4], [1,3], [3, 4], [1, 5], [5, 1]]
    #G = {1:{2}, 2:{3,4}, 3:{4,5}, 4:{1}, 5:{6}, 6:{5}}

    G_rev = reverse_graph(G)
    #G_rev = {1:{4}, 2:{1}, 3:{2}, 4:{2,3}, 5:{3,6}, 6:{5}}
    G = G_dict(G, 4)
    print(G)
    G_rev = G_dict(G_rev, 4)
    print(G_rev)

    leader, f = DFS_loop(G_rev, 4)

    leader, f = DFS_loop(G, 4, f)
    #print(leader)
    l = count_scc(leader)
    print(l)


    #leader = {}
    #DFS_directed_iter(G, 2, set(), f={}, t = [0], leader = leader, current_leader=1)

    #print(leader)


    '''
    #sys.setrecursionlimit(1000000)

    G = []
    with open('SCC.txt', 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            l = list(map(int, line.split()))
            G.append(l)

    G_rev = reverse_graph(G)
    G = G_dict(G, 875714)
    G_rev = G_dict(G_rev, 875714)
    print("hehe")
    
    
    leader, f = DFS_loop(G_rev, 875714)
    leader, f = DFS_loop(G, 875714, f)
    l = count_scc(leader)
    print(l)

