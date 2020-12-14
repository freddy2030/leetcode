from copy import deepcopy

"""
时间复杂度 n^n
"""
def maxSizeSlices(slices):
    if len(slices) <= 3:
        return max(slices)
    maxPiza = 0
    dp = []
    dp.append((slices, 0))
    while len(dp) > 0:
        slices, currentPiza = dp.pop()
        if len(slices) <= 3:
            maxPiza = max(maxPiza, (max(slices) + currentPiza))
        else:
            for i, v in enumerate(slices):
                t = deepcopy(slices)
                if i == (len(slices) - 1):
                    del t[i-1], t[i-1], t[0]
                elif i == 0:
                    del t[-1], t[0], t[0]
                else:
                    del t[i-1], t[i-1], t[i-1]
                dp.append((t, v+currentPiza))
                maxPiza = max(maxPiza, (v+currentPiza))
        
    return maxPiza


if __name__ == "__main__":
    slices = [6,3,1,2,6,2,4,3,10,4,1,4,6,5,5,3,4,7,6,5,8]#,7,3,8,8,1,7,1,7,8]
    res = maxSizeSlices(slices)
    print(res)