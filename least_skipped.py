def least_skipped(arr):
    index_arr = [None] * max(arr)
    for i in range(len(arr)):
        index_arr[arr[i] - 1] = i
    for i in range(len(index_arr)):
        if index_arr[i] == None:
            return i + 1
    return max(arr) + 1
print(least_skipped([3, 1, 2, 4]))
