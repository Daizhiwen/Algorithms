#Strassen algorithm for matrix multiplication
#only for squared matrices with dim n = 2^N
import numpy as np

def divied_mat(X):
    n = X.shape[0]
    A, B, C, D = X[0:n//2, 0:n//2], X[0:n//2, n//2:], X[n//2:, 0:n//2], X[n//2:, n//2:]
    return A, B, C, D

def mat_mut(X, Y):

    if X.shape[0] == 1:
        return X * Y
    else:
        A, B, C, D = divied_mat(X)
        E, F, G, H = divied_mat(Y)
        M1 = mat_mut(A, F - H)
        M2 = mat_mut(A + B, H)
        M3 = mat_mut(C + D, E)
        M4 = mat_mut(D, G - E)
        M5 = mat_mut(A + D, E + H)
        M6 = mat_mut(B - D, G + H)
        M7 = mat_mut(A - C, E + F)

        return np.hstack((np.vstack((M5 + M4 - M2 + M6, M3 + M4)), np.vstack((M1 + M2, M1 + M5 - M3 - M7))))


if __name__ == "__main__":
    X = np.array([[1,2],[3,4]])
    m = mat_mut(X, X)
    print(m)

