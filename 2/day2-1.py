with open('input.txt') as f:
    dirs = [s.split(' ') for s in f.read().splitlines()]

h = 0
v = 0
for dir, val in dirs:
    val = int(val)
    if dir == 'forward':
        h += val
    elif dir == 'up':
        v -= val
    elif dir == 'down':
        v += val

print(h*v)
