with open('input.txt') as f:
    lines = [l.split('->') for l in f.read().splitlines()]
    lines = [(map(int, a.strip().split(',')), map(int, b.strip().split(',')))
             for a, b in lines]

max_x = 0
max_y = 0
for (x1, y1), (x2, y2) in lines:
    max_x = max([max_x, x1, x2])
    max_y = max([max_y, y1, y2])

matrix = [[0 for _ in range(max_x + 1)] for _ in range(max_y + 1)]

for (x1, y1), (x2, y2) in lines:
    min_x, max_x = min(x1, x2), max(x1, x2)
    min_y, max_y = min(y1, y2), max(y1, y2)

    if x1 == x2:
        for i in range(min_y, max_y + 1):
            matrix[i][x1] += 1
    elif y1 == y2:
        for i in range(min_x, max_x + 1):
            matrix[y1][i] += 1
    else:
        slope = (y2 - y1) / (x2 - x1)
        if slope == 1:
            for i in range(max_x - min_x + 1):
                matrix[min_y + i][min_x + i] += 1
        elif slope == -1:
            for i in range(max_x - min_x + 1):
                matrix[max_y - i][min_x + i] += 1

c = 0
for row in matrix:
    for val in row:
        if val >= 2:
            c += 1

print(c)
