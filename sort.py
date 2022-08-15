from random import randrange
from time import time

def quick_sort(A):
    """ Быстрая сортировка """
    if len(A) <= 1:
        return A

    L, M, R = [], [], []

    barrier = A[randrange(len(A))]
    for x in A:
        if x < barrier:
            L.append(x)
        elif x == barrier:
            M.append(x)
        else:
            R.append(x)
    
    return quick_sort(L) + M + quick_sort(R)

def merge_sort(A):
    """ Сортировка слиянием """
    if len(A) <= 1:
        return A
    result = []
    middle = int(len(A) / 2)
    L = merge_sort(A[:middle])
    R = merge_sort(A[middle:])
    i = 0
    j = 0
    while i < len(L) and j < len(R):
        if L[i] > R[j]:
            result.append(R[j])
            j += 1
        else:
            result.append(L[i])
            i += 1
    result += L[i:]
    result += R[j:]
    return result

def insert_sort(A):
    """ Сортировка вставками """
    for top in range(1, len(A)):
        k = top
        while k > 0 and A[k-1] > A[k]:
            A[k], A[k-1] = A[k-1], A[k]
            k -=1

def check_massive_sort_time(A):
    start = time()
    quick_sort(A)
    end = time()
    print(f"quick_sort: {end - start}s")

    start = time()
    merge_sort(A)
    end = time()
    print(f"merge_sort: {end - start}s")
    
    start = time()
    sorted(A)
    end = time()
    print(f"sorted: {end - start}s")


if __name__ == "__main__":
    array_r = [randrange(100000) for i in range(100000)]
    array_s = [i for i in range(100000)]
    array_rs = []
    for i in range(10000):
        array_rs += [i for i in range(10)]
    
    print('Случайный массив')
    check_massive_sort_time(array_r)
    print('Отсортированный массив')
    check_massive_sort_time(array_s)
    start = time()
    insert_sort(array_s)
    end = time()
    print(f"insert_sort: {end - start}s")
    print('Массив из отсортированных частей')
    check_massive_sort_time(array_rs)
