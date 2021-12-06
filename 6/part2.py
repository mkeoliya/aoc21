with open('input.txt') as f:
    lst = [int(v) for v in f.read().splitlines()[0].split(',')]

counts = [0] * 9
for num in lst:
    counts[num] += 1

for day in range(256):
    new_counts = [0] * 9
    for i in range(1, 9):
        new_counts[i - 1] = counts[i]

    # handle counts[0] case
    new_counts[6] += counts[0]
    new_counts[8] = counts[0]
    counts = new_counts

num_fish = sum(counts)
print(num_fish)
