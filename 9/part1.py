with open('input.txt') as f:
    matrix = [[int(char) for char in l] for l in f.read().splitlines()]


m = len(matrix)
n = len(matrix[0])

risk = 0
for i in range(m):
    for j in range(n):
        val = matrix[i][j]

        top = matrix[i-1][j] if i > 0 else float('inf')
        down = matrix[i+1][j] if i < (m - 1) else float('inf')
        left = matrix[i][j - 1] if j > 0 else float('inf')
        right = matrix[i][j + 1] if j < (n - 1) else float('inf')

        if val < top and val < down and val < left and val < right:
            risk += val + 1
            print(val, top, down, left, right)

print(risk)
