from copy import deepcopy

def uniquePaths(m, n):
    score = 0
    dp = []
    # status = []
    chessboard = []
    for i in range(m):
        chessboard.append([0 for i in range(n)])
    
    temp = deepcopy(chessboard)
    temp[0][0] = 1
    dp.append((temp, (0,0)))
    while len(dp) > 0:
        chess, (x,y) = dp.pop()
        print(chess, x, y)
        if (x==(m-1)) & (y==(n-1)):
            score+=1
        else:
            if (x-1)>=0:
                if chess[x-1][y] == 0:
                    temp = deepcopy(chess)
                    temp[x-1][y] = 1
                    dp.append((temp, (x-1, y)))
            if (x+1)<m:
                if chess[x+1][y] == 0:
                    temp = deepcopy(chess)
                    temp[x+1][y] = 1
                    dp.append((temp, (x+1, y)))
            if (y-1)>=0:   
                if chess[x][y-1] == 0:
                    temp = deepcopy(chess)
                    temp[x][y-1] = 1
                    dp.append((temp, (x, y-1)))
            if (y+1)<n:
                if chess[x][y+1] == 0:
                    temp = deepcopy(chess)
                    temp[x][y+1] = 1
                    dp.append((temp, (x, y+1)))
    return score


if __name__ == "__main__":
    m, n = (3, 2)
    s = uniquePaths(m, n)
    print(s)