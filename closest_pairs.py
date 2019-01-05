import merge_sort
class point():
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

def points_to_XY(P):
    X = []
    Y = []
    for i in range(len(P)):
        X.append(P[i].x)
        Y.append(P[i].y)

    return X, Y

def divide_points(X, Y):
    Px = merge_sort.div_merge(X)