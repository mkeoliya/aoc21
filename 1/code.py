with open('file.txt') as f:
    nums = [int(line.strip()) for line in f.readlines()]

prev = nums[0]
c = 0
window_sum = nums[0] + nums
for num in nums[1:]:
    if num > prev:
        c += 1
    prev = num

print(c)
