from copy import deepcopy

def maxSizeSlices(slices):
    if len(slices) <= 3:
        return max(slices)
    maxPiza = 0
    dp = []
    dp.append((slices, 0))
    while len(dp) > 0:
        slices, currentPiza = dp.pop()
        for i, v in enumerate(slices):
            t = deepcopy(slices)
            if len(t) <= 3:
                maxPiza = max(maxPiza, max(t) + currentPiza)
            else:
                if i == (len(slices) - 1):
                    del t[i-1], t[i-1], t[-1]
                elif i == 0:
                    del t[-1], t[0], t[0]
                else:
                    del t[i-1], t[i-1], t[i-1]
                dp.append((t, v+currentPiza))
                maxPiza = max(maxPiza, currentPiza)
    return maxPiza


if __name__ == "__main__":
    slices = [1,2,3,4,5,6]
    res = maxSizeSlices(slices)
    print(res)