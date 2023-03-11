def bubble(array): # сортировка пузырьком
    for i in range(0, len(array)):
        for j in range(len(array)-1, i, -1):
            if array[j-1] > array[j]:
                array[j-1], array[j] = array[j], array[j-1]
    return array

def shaker(array): # сортировка шейкером
    k = len(array)-1
    lb = 1
    ub = len(array)-1
    while True:
        for j in range(ub, 0, -1):
            if array[j-1] > array[j]:
                array[j-1], array[j] = array[j], array[j-1]
                k = j
        lb = k+1
        for j in range(1, ub+1):
            if array[j-1] > array[j]:
                array[j-1], array[j] = array[j], array[j-1]
                k = j
        ub = k-1
        if not lb < ub:
            break
    return array

def merge(array, low, mid, high): # сортировка слиянием
    b = [None]*(high+1-low)
    h = low
    i = 0
    j = mid+1
    while h <= mid and j <= high:
        if array[h] <= array[j]:
            b[i] = array[h]
            h += 1
        else:
            b[i] = array[j]
            j += 1
        i += 1
    if h > mid:
        for k in range(j, high+1):
            b[i] = array[k]
            i += 1
    else:
        for k in range(h, mid+1):
            b[i] = array[k]
            i += 1
    for k in range(high-low+1):
        array[k+low] = b[k]
    return array

def merge_sort(array, low, high):
    if low < high:
        mid = (low+high)//2
        merge_sort(array, low, mid)
        merge_sort(array, mid+1, high)
        merge(array, low, mid, high)
    return array