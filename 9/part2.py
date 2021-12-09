with open('input.txt') as f:
    matrix = [[int(char) for char in l] for l in f.read().splitlines()]
    visited = [[False for _ in l] for l in matrix]


m = len(matrix)
n = len(matrix[0])


def find_basin(i, j):
    if i < 0 or i >= m or j < 0 or j >= n or visited[i][j] or matrix[i][j] == 9:
        return 0

    visited[i][j] = True

    return 1 + find_basin(i - 1, j) + find_basin(i + 1, j) + find_basin(i, j - 1) + find_basin(i, j + 1)


basins = []
for i in range(m):
    for j in range(n):
        val = matrix[i][j]

        top = matrix[i-1][j] if i > 0 else float('inf')
        down = matrix[i+1][j] if i < (m - 1) else float('inf')
        left = matrix[i][j - 1] if j > 0 else float('inf')
        right = matrix[i][j + 1] if j < (n - 1) else float('inf')

        if val < top and val < down and val < left and val < right:
            basins.append(find_basin(i, j))

basins = sorted(basins)
print(basins[-1] * basins[-2] * basins[-3])
