import numpy as np

# np.random.seed(19680803)
def O3n(n: int) -> int:
    '''стоимость проезда считается так - 
    значение массива * удаленность от заданной точки (модуль разности индексов)
    от какой точки суммарная стоимость проезда до каждой точки будет максимальной?
    '''
    arr = list(np.random.rand(n))

    pref = [0]
    for e in arr:
        pref.append(e + pref[-1])
    pref = pref[1:]

    suff = [0]
    for e in reversed(arr):
        suff.append(e + suff[-1])
    suff.reverse()
    suff = suff[:-1]

    summ = sum([arr[e] * e for e in range(len(arr))])
    mi = summ
    for e in range(1, len(arr)):
        summ = summ + pref[e - 1] - suff[e]
        mi = min(summ, mi)

    return arr, mi


def Onlogn(n: int):
    '''мердж сорт'''
    def merge_sort(arr: list) -> list:
        if len(arr) in [0, 1]:
            return arr
        left = merge_sort(arr[:len(arr) // 2])
        right = merge_sort(arr[len(arr) // 2:])
        merged = []
        l_i, r_i = 0, 0
        while l_i < len(left) and r_i < len(right):
            if left[l_i] < right[r_i]:
                merged.append(left[l_i])
                l_i += 1
            else:
                merged.append(right[r_i])
                r_i += 1
        if l_i >= len(left):
            for e in range(r_i, len(right)):
                merged.append(right[e])
        else:
            for e in range(l_i, len(left)):
                merged.append(left[e])
        return merged
    
    arr = list(np.random.rand(n))
    return arr, merge_sort(arr)
    

def Ofact(n: int):
    '''получение всех возможных путей графа, содержаших все вершины не более одного раза'''
    arr = np.random.randint(2, size=(n, n))
    all_paths = []
    def recursive_walk(cur_vert: int, used_verts: list):
        if set([e for e in range(n) if arr[cur_vert, e]]) - set(used_verts) == set():
            all_paths.append(used_verts.copy())
            return
        for next_vert in range(n):
            if next_vert not in used_verts and arr[cur_vert, next_vert]:
                recursive_walk(next_vert, used_verts + [next_vert])
    for start_vert in range(n):
        recursive_walk(start_vert, [start_vert])
    return arr, all_paths
        

def On3(n):
    '''флгоритм флойда уоршела'''
    edges = np.random.randint(n, size=(int(n ** 1.5), 2))
    weights = np.random.randint(100, size=(int(n ** 1.5), 1))
    arr = np.append(edges, weights, 1)
    dist = np.full((n, n), np.inf)
    for e in range(n):
        dist[e][e] = 0
    for e in range(len(arr)):
        if dist[arr[e][0], arr[e][1]] > arr[e][2]:
            dist[arr[e][0], arr[e][1]] = arr[e][2]
        if dist[arr[e][1], arr[e][0]] > arr[e][2]:
            dist[arr[e][1], arr[e][0]] = arr[e][2]
    for e in range(n):
        for j in range(n):
            for i in range(n):
                if dist[j][e] + dist[e][i] < dist[j][i]:
                    dist[j][i] = dist[j][e] + dist[e][i]
    return arr, dist


def binary_search(arr: list[int], obj: int) -> int:
    # binary search in sorted int-list
    l, r = 0, len(arr) - 1
    while l < r + 1:
        m = (l + r) // 2
        if obj == arr[m]:
            return m
        elif obj < arr[m]:
            r = m - 1
        else:
            l = m + 1
    return -1


def O3logn(n):
    arr = sorted(list(np.random.randint(10 * n, size=n)))
    f1, f2, f3 = [arr[np.random.randint(n)] if np.random.randint(2) 
                  else np.random.randint(100 * n) for e in range(3)]
    return arr, [f1, f2, f3], [binary_search(arr, f) for f in [f1, f2, f3]]
    
            