import time
import math
import functools
"""
回溯 超时
"""
def coinChange(coins, amount):
    # coins.sort(reverse=True)
    dp = []
    min_n = float('inf')
    dp.append((0,11))
    while len(dp)>0:
        n, rest = dp.pop()
        print(n, rest)
        if rest == 0:
            min_n = min(n, min_n)
        else:
            for i in coins:
                if i <= rest:
                    dp.append((n+1, rest-i))
    
    if min_n == float('inf'):
        min_n = -1
    return min_n

"""
方法二
"""
def coinChange1(coins, amount):
    dp = {}
    for i in coins:
        dp[i] = 1

    def coin(amount):
        # print("@34", amount)
        if amount < 0:
            return -1
        if amount == 0:
            return 0
        if amount in dp.keys():
            if dp[amount] != math.pow(10, 4):
                return dp[amount]
        else:
            dp[amount] = math.pow(10,4)
        # rest = list(filter(lambda x: x!= -1,list(map(lambda x: coin(amount-x),coins))))
        # print(amount, "   ", rest)
        # return min(rest) + 1
        min_n = dp[amount]
        for i in coins:
            if i < amount:
                n = coin(amount-i) + 1
                if (n != -1) & (n < min_n):
                    min_n = n
        if min_n == math.pow(10, 4):
            min_n = -1
        dp[amount] = min_n
        print(dp)
        return min_n
    return coin(amount)

def coinChange2(coins, amount):
    @functools.lru_cache(amount)
    def dp(rem):
        if rem < 0: return -1
        if rem == 0: return 0
        mini = int(1e9)
        for coin in coins:
            res = dp(rem - coin)
            if res >= 0 and res < mini:
                mini = res + 1
        return mini if mini < int(1e9) else -1

    # coins = coins
    if amount < 1: return 0
    return dp(amount)
    


if __name__ == "__main__":
    coins = [1,2,5]
    amount = 31
    # n = coinChange(coins, amount)
    time1 = time.time()
    n = coinChange1(coins, amount)
    print("用时：", time.time() - time1)
    print(n)