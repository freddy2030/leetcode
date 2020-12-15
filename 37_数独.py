from copy import deepcopy

"""
注意board里的数字为string
"""

def solveSudoku(board):
    """
    return (i,j) or None
    """
    def isFinished(board):
        for i, v1 in enumerate(board):
            for j, v2 in enumerate(v1):
                if v2 == ".":
                    return (i,j)

    def validNumber(board, loc):

        all_number = [i for i in range(1, 10)]

        for i in board[loc[0]]:
            if i != ".":
                if int(i) in all_number:
                    all_number.remove(int(i))

        for i in range(len(board)):
            v = board[i][loc[1]]
            if v != ".":
                if int(v) in all_number:
                    all_number.remove(int(v))
        
        row = loc[0]//3  # 3x3宫序号
        col = loc[1]//3
        for i in range(row*3, (row+1)*3):
            for j in range(col*3, (col+1)*3):
                v = board[i][j]
                if v != ".":
                    if int(v) in all_number:
                        all_number.remove(int(v))
        return all_number

    dp = []
    dp.append(board)
    while len(dp) > 0:
        current_board = dp.pop()
        next_loc = isFinished(current_board)
        if next_loc == None:
            return current_board
        else:
            valid_number = validNumber(current_board, next_loc)
            for i in valid_number:
                temp_board = deepcopy(current_board)
                temp_board[next_loc[0]][next_loc[1]] = str(i)
                dp.append(temp_board)
    return good
    
    



if __name__ == "__main__":
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    good = solveSudoku(board)
    print(good)