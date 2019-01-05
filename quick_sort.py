from numpy.random import randint

def choose_pivot(l, r):
    #choose the pivot randomly
    p = randint(l, r)
    #print(p)

    p = l
    return p


def partition(list, p, l, r):

    list[p], list[l] = list[l], list[p]
    i = l + 1
    for j in range(l + 1, r):
        if list[j] < list[l]:
            list[i], list[j] = list[j], list[i]
            i += 1
    list[i - 1], list[l] = list[l], list[i - 1]
    #return the new position of pivot
    return i - 1

def quick_sort(list, l, r):
    #print(l, r)
    if r - l <= 1:
        return
    else:
        #p is the position of the pivot
        p = choose_pivot(l, r)
        #update p
        p = partition(list, p, l, r)
        quick_sort(list, l, p)
        quick_sort(list, p + 1, r)

if __name__ == "__main__":
    l = [3,4,7,31,23,2,1,99, -1, 99]
    #partition(l, 0, 0, len(l))
    #print(l)

    quick_sort(l,0, len(l))
    print(l)