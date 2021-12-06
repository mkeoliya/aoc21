with open('input.txt') as f:
    lst = [int(v) for v in f.read().splitlines()[0].split(',')]

for day in range(256):
    next_lst = []
    while lst:
        fish = lst.pop()
        if fish > 0:
            next_lst.append(fish - 1)
        else:
            next_lst.append(6)
            next_lst.append(8)

    lst = next_lst

num_fish = len(lst)
print(num_fish)
