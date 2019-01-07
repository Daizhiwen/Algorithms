import numpy

def partition(list, p):
    l =0
    r = len(list)

    #list = list.copy()
    list[p], list[l] = list[l], list[p]
    i = l + 1
    for j in range(l + 1, r):
        #c[0] += 1

        if list[j] < list[l]:
            list[i], list[j] = list[j], list[i]
            i += 1
    list[i - 1], list[l] = list[l], list[i - 1]
    #return the new position of pivot
    return i - 1, list[l: i - 1], list[i: r]

def choose_pivot(list):
    #choose the pivot randomly
    l = 0
    r = len(list)
    #p = randint(l, r)
    #print(p)

    p1 = l
    p3 = r - 1
    p2 = (l + r - 1)//2

    #print(p1, p2, p3)

    med = int(numpy.median([list[p1], list[p2], list[p3]]))
    for i in [p1, p2, p3]:
        if list[i] == med:
            break
    return i

def rand_select(list, i):

    if len(list) == 1:
        return list[0]

    p = choose_pivot(list)
    p, list_l, list_r = partition(list, p)
    #print(p, list_l, list_r)

    if p == i:
        return list[p]
    elif p < i:
        return rand_select(list_r, i - p - 1)
    else:
        return rand_select(list_l, i)


if __name__ == "__main__":
    list = [7,6,5,4,3,2,1,0]
    i = rand_select(list.copy(), 5)
    print(i)
    print(list)
