import numpy as np


def heap_sort(arr):
    sequence = arr[:]
    def sift_down(parent, limit):
        item = sequence[parent]
        while True:
            child = (parent * 2) + 1
            if child >= limit:
                break
            if child + 1 < limit and sequence[child] < sequence[child + 1]:
                child += 1
            if item < sequence[child]:
                sequence[parent] = sequence[child]
                parent = child
            else:
                break
        sequence[parent] = item
    length = len(sequence)
    for index in range((length // 2) - 1, -1, -1):
        sift_down(index, length)
    for index in range(length - 1, 0, -1):
        sequence[0], sequence[index] = sequence[index], sequence[0]
        sift_down(0, index)
    return sequence


def bucket_sort(arr, minElement="", maxElement="", numBuckets=10):
    if minElement == "":
        minElement = min(arr)
    if maxElement == "":
        maxElement = max(arr)
    if len(arr) < 2 or minElement == maxElement:
        return arr
    diff = maxElement - minElement
    buckets = [[] for _ in range(numBuckets)]
    minBuckets = [np.inf for _ in range(numBuckets)]
    maxBuckets = [-np.inf for _ in range(numBuckets)]
    for e in range(len(arr)):
        if arr[e] == maxElement:
            index = numBuckets - 1
        else:
            index = int(numBuckets - (maxElement - arr[e]) * numBuckets / diff)
        buckets[index].append(arr[e])
        minBuckets[index] = min(minBuckets[index], arr[e])
        maxBuckets[index] = max(minBuckets[index], arr[e])
    for e in range(numBuckets):
        buckets[e] = bucket_sort(buckets[e], minBuckets[e], maxBuckets[e], numBuckets)
    result = []
    for e in range(numBuckets):
        for j in range(len(buckets[e])):
            result.append(buckets[e][j])
    return result


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


def test(a1, a2, size, func):
    a = list(np.random.randint(a1, a2, size=size))
    return a, func(a)


print(*test(1, 100, 10, bucket_sort), sep="\n")
print()
print(*test(1, 100, 10, heap_sort), sep="\n")
print()
print(*test(1, 100, 10, merge_sort), sep="\n")
