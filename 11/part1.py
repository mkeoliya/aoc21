with open('input.txt') as f:
    matrix = [[int(c) for c in l]for l in f.read().splitlines()]


def flash(i, j, has_flashed):
    if i < 0 or i == 10 or j < 0 or j == 10 or has_flashed[i][j]:
        return

    matrix[i][j] += 1

    if matrix[i][j] > 9:
        has_flashed[i][j] = True
        flash(i - 1, j, has_flashed)
        flash(i + 1, j, has_flashed)
        flash(i, j - 1, has_flashed)
        flash(i, j + 1, has_flashed)
        flash(i - 1, j - 1, has_flashed)
        flash(i - 1, j + 1, has_flashed)
        flash(i + 1, j - 1, has_flashed)
        flash(i + 1, j + 1, has_flashed)


steps = 0
while True:
    steps += 1
    has_flashed = [[False for c in l]for l in matrix]
    for i in range(10):
        for j in range(10):
            matrix[i][j] += 1
    for i in range(10):
        for j in range(10):
            if matrix[i][j] > 9:
                flash(i, j, has_flashed)

    flashes = 0
    for i in range(10):
        for j in range(10):
            if has_flashed[i][j]:
                matrix[i][j] = 0
                flashes += 1

    if flashes == 100:
        break


print(steps)
