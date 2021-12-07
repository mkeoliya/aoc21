with open('input.txt') as f:
    a = [int(v) for v in f.read().splitlines()[0].split(',')]

min_h = min(a)
max_h = max(a)
min_horiz = float('inf')
for num in range(min_h, max_h):
    sum_curr = 0
    for num_j in a:
        sum_curr += abs(num_j - num)
    min_horiz = min([min_horiz, sum_curr])

print(min_horiz)
