def canPlaceFlowers(flowerbed, n):
    max_n = 0
    for i in range(len(flowerbed)):
        if i == 0:
            if (flowerbed[i] == 0) & (flowerbed[i+1] == 0):
                max_n += 1
                flowerbed[i] = 1
        elif i == (len(flowerbed)-1):
            if (flowerbed[i] == 0) & (flowerbed[i-1] == 0):
                max_n += 1
                flowerbed[i] = 1
        else:
            if (flowerbed[i] == 0) & (flowerbed[i-1] == 0) & (flowerbed[i+1] == 0):
                max_n += 1
                flowerbed[i] = 1

    return (max_n >= n)

if __name__ == "__main__":
    flowerbed = [1,0,0,0,1]
    n = 1
    result = canPlaceFlowers(flowerbed, n)
    print(result)