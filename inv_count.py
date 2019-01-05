#count the inversions in an array of integers
#based on merge sort algorithm
import numpy as np
def merge(list1, list2):
    i = 0
    j = 0
    count = 0
    out = []
    for k in range(len(list1 + list2)):
        if list1[i] <= list2[j]:
            out.append(list1[i])
            i += 1
            if i == len(list1):
                out.extend(list2[j:])
                return out, count
        else:
            out.append(list2[j])
            j += 1
            count += len(list1) - i
            if j == len(list2):
                out.extend(list1[i:])
                return out, count
    return out, count


def divide(list):
    n = len(list)
    return list[0:n//2], list[n//2:]

def inv_count(list):
    if len(list) == 1:
        return list, 0
    else:
        list1, list2 = divide(list)
        #print(list1, list2)
        list1_sorted, count1 = inv_count(list1)
        list2_sorted, count2 = inv_count(list2)
        list_sorted, count_cross = merge(list1_sorted, list2_sorted)
        return list_sorted, count1 + count2 + count_cross



if __name__ == "__main__":
    data = np.loadtxt("a.txt")
    list = data.tolist()
    s, count = inv_count(list)
    print(count)