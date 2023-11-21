from math import inf

v = [10, 20, 30, 5, 8, 90, 4]
n = len(v)
dp = [[-1 for j in range(n)] for e in range(n)] 

def matrixChainMultiplication(l, r): 
    if dp[l][r] == -1:   
        if l == r - 1:
            dp[l][r] = 0
        else:
            dp[l][r] = inf
            for i in range(l + 1, r):
                dp[l][r] = min(dp[l][r], v[l] * v[i] * v[r] +  matrixChainMultiplication(l, i) + matrixChainMultiplication(i, r))
    return dp[l][r]

print(matrixChainMultiplication(0, n - 1))