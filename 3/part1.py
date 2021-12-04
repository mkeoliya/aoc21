
with open('input.txt') as f:
    nums = f.read().splitlines()

bits = [0] * 12
for num in nums:
    for i, char in enumerate(num):
        if char == '1':
            bits[i] += 1

gamma = [round(c/len(nums)) for c in bits]
epsilon = [0 if b else 1 for b in gamma]

gammma_int = int("".join(str(x) for x in gamma), 2)
epsilon_int = int("".join(str(x) for x in epsilon), 2)

print(gammma_int * epsilon_int)
