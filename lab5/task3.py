import numpy as np

N = 10
arr = np.random.randint(-100, 100, size=N)
old = arr[0]
ma_x = 0
ma_y = 0
fi = 0

for e in range(1, N):
    if old >= arr[e]:
        if ma_y - ma_x + 1 < e - fi:
            ma_y = e - 1
            ma_x = fi
        fi = e
    old = arr[e]
if ma_y - ma_x + 1 < N - fi:
    ma_y = N - 1
    ma_x = fi
print(arr)
print(arr[ma_x:ma_y + 1]) 