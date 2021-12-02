with open('input.txt') as f:
    dirs = [s.split(' ') for s in f.read().splitlines()]

h = 0
v = 0
aim = 0
for dir, val in dirs:
    val = int(val)
    if dir == 'forward':
        h += val
        v += aim * val
    elif dir == 'up':
        aim -= val
    elif dir == 'down':
        aim += val

print(h*v)
