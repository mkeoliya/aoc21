from collections import Counter

with open('input.txt') as f:
    a = f.read().splitlines()
    template = a[0]
    lst = {line.split(' -> ')[0]: line.split(' -> ')[1] for line in a[2:]}

for step in range(10):
    new_template = template
    i = 1
    ins = 0
    while i < len(template):
        pair = template[i - 1] + template[i]
        if pair in lst:
            new_template = new_template[:i + ins] + \
                lst[pair] + new_template[i + ins:]
            ins += 1
        i += 1

    template = new_template

c = Counter(template)
max_e = max(template, key=template.count)
min_e = min(template, key=template.count)

print(c[max_e] - c[min_e])
