# Leetcode - 1
# Brute force: 
# time comp: O(n^2)
def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i]+nums[j] == target:
                return [i, j]
nums = list(map(int, input("Enter array of elements: ").split()))
target = int(input("Enter target value: "))
result = twoSum(nums, target)
if result:
    print(f"Indices of nums that add up to {target}: {result}")
else:
    print(f"No two nums add to target.")

