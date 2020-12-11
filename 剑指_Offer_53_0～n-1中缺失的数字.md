# 题目
> 一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。
## 解法 1
> 执行用时：40 ms, 在所有 Python3 提交中击败了91.66%的用户
> 
> 内存消耗：14.7 MB MB, 在所有 Python3 提交中击败了46.24%的用户
### *代码*
```
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        p_start = 0
        p_end = len(nums) - 1
        p = len(nums)//2
        while True:
            if p_start == p_end:
                if nums[p] == p:
                    return p+1
                else:
                    return p

            if nums[p] > p:
                p_end = p - 1
                if p_end < p_start:
                    p_end = p_start
            else:
                p_start = p + 1
                if p_start > p_end:
                    p_start = p_end
            p = (p_start + p_end) // 2
```