from jump_input_54 import nums
import sys

"""
递归炸了
"""
def jump(nums) -> int:
    jump_cache = {}
    def subJump(nums, end: int):
        min_jump_count = len(nums)
        if end == 0:
            return 0

        if end in jump_cache.keys():
            return jump_cache[end]

        for i in range(0, end):
            if nums[i] >= (end-i):
                c = subJump(nums, i)
                if c != None:
                    min_jump_count = min(c+1, min_jump_count)
                    break
        jump_cache[end] = min_jump_count
        return min_jump_count

    return subJump(nums,len(nums)-1)

def jump1(nums) -> int:
    dp = [nums[0]]
    max_touch = nums[0]

    for i in range(1, len(nums)):
        if dp[-1] >= (len(nums)-1):
            return len(dp)

        if i <= dp[-1]:
            max_touch = max(max_touch, nums[i] + i)

        if i == dp[-1]:
            dp.append(max_touch)



if __name__ == "__main__":
    # nums = [2,3,1,1,4,1]
    # print(len(nums))
    # sys.setrecursionlimit(len(nums)*2)
    result = jump1(nums)

    print(result)