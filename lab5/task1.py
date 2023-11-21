def find_knapSack(max_weight, weights, profits):
    N = len(weights)
    table = [[0 for x in range(max_weight + 1)] for x in range(N + 1)]

    for e in range(1, N + 1):
        for j in range(max_weight + 1):
            weight = weights[e - 1]
            profit = profits[e - 1]
            table[e][j] = table[e - 1][j]
            if weight <= j:
                table[e][j] = max(table[e][j], table[e - 1][j - weight] + profit)

    result = []
    for e in range(N, 0, -1):
        if table[e][max_weight] != table[e - 1][max_weight]:
            result.append(e - 1)
            max_weight -= weights[e - 1]
    return result


if __name__ == "__main__":
    profits = [60, 100, 120, 100, 50]
    weights = [10, 20, 30, 20, 10]
    knapsacks = [30, 30]
    arr = []
    N = len(profits)
    for knapsack in knapsacks:
        inds = find_knapSack(knapsack, weights, profits)
        arr.append(0)
        for ind in inds:
            arr[-1] += profits[ind]
        for ind in inds:
            del profits[ind]
            del weights[ind]
    print(*arr)
