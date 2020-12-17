import random

class Solution:

    def __init__(self, nums):
        self.nums = nums

    def pick(self, target: int) -> int:
        index = None
        n = 0
        for i, v in enumerate(self.nums):
            if v == target:
                n += 1
                if random.random() < (1/n):
                    index = i
        
        return index


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)