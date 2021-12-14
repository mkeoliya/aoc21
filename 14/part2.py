from collections import Counter
from itertools import *

with open('input.txt') as f:
    a = f.read().splitlines()
    template = a[0]
    rules = {line.split(' -> ')[0]: line.split(' -> ')[1] for line in a[2:]}
    char_set = set()
    for pair, ele in rules.items():
        char_set.add(pair[0])
        char_set.add(pair[1])
        char_set.add(ele)

perms = [p for p in product(char_set, repeat=2)]
counts = Counter(template)
perms_map = {a+b: 0 for (a, b) in perms}


for a, b in zip(template, template[1:]):
    perms_map[a + b] += 1

for step in range(40):
    new_perms_map = perms_map.copy()
    for pair, _ in perms_map.items():
        cnt = perms_map[pair]
        if pair in rules and cnt > 0:
            ele = rules[pair]
            pair1 = pair[0] + ele
            pair2 = ele + pair[1]

            new_perms_map[pair] -= cnt
            new_perms_map[pair1] += cnt
            new_perms_map[pair2] += cnt

            counts.update({ele: perms_map[pair]})

    perms_map = new_perms_map

max_e = max(counts.values())
min_e = min(counts.values())

print(max_e - min_e)
