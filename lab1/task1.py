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

if __name__ == "__main__":
    arr = [1, 7, 8, 11, 12]
    print(binary_search(arr, 12))
    print(binary_search(arr, 3))