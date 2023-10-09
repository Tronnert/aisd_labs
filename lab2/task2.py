def bubble_sort(arr):
    result = arr.copy()
    ready = False
    while not ready:
        ready = True
        for i in range(len(arr) - 1):
            if result[i] > result[i + 1]:
                ready = False
                val = result[i]
                result[i] = result[i + 1]
                result[i + 1] = val
    return result
