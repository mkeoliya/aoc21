with open('file.txt') as f:
    nums = [int(line.strip()) for line in f.readlines()]

c = 0
window_sum = nums[0] + nums[1] + nums[2]
for i, num in enumerate(nums[3:]):
    new_window_sum = window_sum + num - nums[i]
    if new_window_sum > window_sum:
        c += 1
    window_sum = new_window_sum

print(c)
