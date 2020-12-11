from typing import List, Sequence

def maxProduct(nums: List[int]) -> int:
    max_val = nums[0]
    imax =  nums[0]
    imin = nums[0]
    for i in range(1, len(nums)):
        print(imax, " ", imin, " ", nums[i])
        if nums[i] < 0:
            t = imax
            imax = imin
            imin = t
        imax = max(nums[i], nums[i]*imax)
        imin = min(nums[i], nums[i]*imin)
        print(imax, " ", imin, " ", nums[i])
        max_val = max(max_val, imax)
    return max_val

src = [-1,-2,-9,-6]
result = maxProduct(src)
print(result)