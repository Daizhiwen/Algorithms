from numpy.random import randint
from numpy import loadtxt
import numpy

def choose_pivot(list, l, r):
    #choose the pivot randomly
    #p = randint(l, r)
    #print(p)

    p1 = l
    p3 = r - 1
    p2 = (l + r - 1)//2

    med = int(numpy.median([list[p1], list[p2], list[p3]]))
    for i in [p1, p2, p3]:
        if list[i] == med:
            break
    return i


def partition(list, p, l, r, c):
    list[p], list[l] = list[l], list[p]
    i = l + 1
    for j in range(l + 1, r):
        c[0] += 1

        if list[j] < list[l]:
            list[i], list[j] = list[j], list[i]
            i += 1
    list[i - 1], list[l] = list[l], list[i - 1]
    #return the new position of pivot
    return i - 1

def quick_sort(list, l, r, c):
    #print(l, r)
    if r - l <= 1:
        return
    else:
        #p is the position of the pivot
        p = choose_pivot(list, l, r)
        #update p
        p = partition(list, p, l, r, c)
        print(c)
        quick_sort(list, l, p, c)
        quick_sort(list, p + 1, r, c)

if __name__ == "__main__":
    data = loadtxt("QuickSort.txt")
    list = data.tolist()

    c = [0]
    quick_sort(list, 0, len(list), c)
