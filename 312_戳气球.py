from copy import deepcopy

"""
复杂度n!
遍历所有情况
挑选一个气球 x，做为第一次点爆的气球
第一步：n 种情况，分别戳 0 - n-1 号气球
第二步：每种情况分为 n-1 种，
。。。
第n步：只剩最后一个气球，返回值
"""
def maxCoins(nums) -> int:
    cache = {}
    def getCoin(nums, i):
        if i == 0:
            return nums[0] * nums[1]
        elif i == len(nums)-1:
            return nums[i] * nums[i-1]
        else:
            return nums[i-1] * nums[i] * nums[i+1]

    def coin(nums):
        if len(nums) == 1:
            return nums[0]
        if str(nums) in cache.keys():
            return cache[str(nums)]
        max_coin = 0
        for i, v in enumerate(nums):
            sub_nums = deepcopy(nums)
            del sub_nums[i]
            max_coin = max(max_coin, getCoin(nums, i) + coin(sub_nums))
        cache[str(nums)] = max_coin
        return max_coin

    return coin(nums)

"""
第一次挑选一个气球，作为最后一次电爆的气球
"""
def maxCoins1(nums) -> int:
    n = len(nums)
    cache = [[-1]*(n+2) for _ in range(n+2)]
    nums.insert(0,1)
    nums.append(1)
    def coin(left, right):
        if left+1 >= right:
            return 0
        if cache[left][right] != -1:
            return cache[left][right]
        max_coin = 0
        for k in range(left+1, right):
            t = nums[left] * nums[k] * nums[right]
            t += (coin(left,k) + coin(k, right))
            max_coin = max(max_coin, t)
        cache[left][right] = max_coin
        return max_coin
    return coin(0, n+1)


if __name__ == "__main__":
    nums = [5,8]
    # nums = [35,16,83,87,84,59,48,41,20,54]
    # nums = [8,2,6,8,9,8,1,4,1,5,3,0,7,7,0,4,2,2]
    import time
    start_time = time.time()
    result = maxCoins1(nums)
    print(result)
    # print(time.time()-start_time)