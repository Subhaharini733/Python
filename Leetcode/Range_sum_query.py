# Leetcode - 303 - Range sum query -immutable
# time comp for initialization is O(n) and sumrange is O(1)
# space comp for self.prefix list is O(n)

class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []
        count = 0
        for i in nums:
            count += i
            self.prefix.append(count)

    def sumRange(self, left: int, right: int) -> int:
        right_ele = self.prefix[right]
        left_ele = self.prefix[left - 1]
        if left > 0:
            return right_ele - left_ele
        else:
            return right_ele
# Explanation:
# using prefix sumapproach first add elementsand append it to prefx list created
# then in summrange check if left >0 , if yes then subtract (left-1) from right 
# if left < = 0 , then return 0

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
