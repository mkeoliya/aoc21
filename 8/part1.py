with open('input.txt') as f:
    a = [line.split(' | ')[1] for line in f.read().splitlines()]

entries = [line.split() for line in a]

c = 0
for lst in entries:
    for term in lst:
        if len(term) == 2 or len(term) == 3 or len(term) == 4 or len(term) == 7:
            c += 1

print(c)
