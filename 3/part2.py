
with open('input.txt') as f:
    nums = f.read().splitlines()


def get_rating(nums, is_oxygen=True):
    for i in range(12):
        if len(nums) == 1:
            break

        ones = [num for num in nums if num[i] == '1']
        not_ones = [num for num in nums if num not in ones]

        if len(ones) >= len(nums) / 2:
            nums = ones if is_oxygen else not_ones
        else:
            nums = not_ones if is_oxygen else ones

    return nums[0]


oxygen = int(get_rating(nums, is_oxygen=True), 2)
co2 = int(get_rating(nums, is_oxygen=False), 2)

print(oxygen * co2)
