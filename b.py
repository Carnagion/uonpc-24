from itertools import permutations

digits = input()
n = int(digits)

nums = [int("".join(num))
        for num in permutations(digits) if int("".join(num)) > n]
nums.sort()

print(0 if len(nums) == 0 else nums[0])
