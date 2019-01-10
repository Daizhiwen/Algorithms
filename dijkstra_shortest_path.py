import numpy as np
def dijkstra(G, s):
    X = {s}
    A = {}
    B = {}
    A[s] = 0
    B[s] = [s]
    while len(G) != len(X):
        print(X, B)
        C = np.array([[0,0,np.infty]])
        for v in X:
            for w, distance in G[v]:
                if w not in X:
                    row = np.array([[v, w, A[v] + distance]])
                    C = np.r_[C, row]
        if C.shape[0] == 1:
            #no path from X to V - X
            for w in G:
                if w not in X:
                    A[w] = 1000000
                    B[w] = None
            return A, B

        #find the min [v*, w*, l*]
        index = np.argmin(C[:, 2])
        #print(index)
        #index = index[0]
        v_s, w_s, l_s = map(int, C[index, :])
        print(v_s, w_s, l_s)
        #add w* to X
        X.add(w_s)
        A[w_s] = l_s
        B[w_s] = B[v_s].copy()
        B[w_s].append(w_s)

    return A, B

if __name__ == "__main__":
    #G = {1:[[2,2], [3, 4]], 2:[[3, 5], [1, 2]], 3:[[2, 5], [1, 4]], 4:[[5, 1]], 5:[[4, 1]]}

    G = {}
    with open('dijkstraData.txt', 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            l = line.split()
            edges= [list(map(int, i.split(","))) for i in l[1:]]
            print(edges)
            G[int(l[0])] = edges


    A, B = dijkstra(G, 1)
    print(A)
    print(B)




