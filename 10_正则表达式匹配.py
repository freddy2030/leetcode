import time
def isMatch(s: str, p: str) -> bool:

    def generatePStack(p):
        p_stack = []
        star_flag = False
        i = len(p)
        while i > 0:
            i -= 1
            c = p[i]
            if star_flag:
                p_stack.append(c+'*')
                star_flag = False
            else:
                if ((ord(c)>=97) & (ord(c)<=122)) | (c=="."):
                    p_stack.append(c)
                else:
                    star_flag = True
        p_stack.reverse()
        return p_stack

    def isPCouldNone(j, p):
        for i in range(j, len(p)):
            if len(p[i]) != 2:
                return False
        return True
    
    def removePSameItem(p):
        temp = []
        for i in p:
            if len(i) == 1:
                temp.append(i)
            else:
                if i[0] == '.':
                    while len(temp) > 0:
                        if len(temp[-1]) == 1:
                            break
                        else:
                            temp.pop()
                    temp.append(i)
                else:
                    if len(temp) == 0:
                        temp.append(i)
                    else:
                        if (len(temp[-1]) == 1)|((temp[-1][0] != i[0]) & (temp[-1][0] != '.')):
                            temp.append(i)
        return temp

    def isSubjectMatch(i, j, s, p):
        flag = False
        if i < len(s):
            if j < len(p):
                if len(p[j]) == 1:
                    if (s[i] == p[j][0]) | (p[j][0] == '.'):
                        flag = isSubjectMatch(i+1, j+1, s, p)
                    else:
                        flag = False
                else:
                    if (s[i] == p[j][0]) | (p[j][0] == '.'):
                        flag = isSubjectMatch(i+1, j+1, s, p) | isSubjectMatch(i+1, j, s, p) | isSubjectMatch(i, j+1, s, p)
                    else:
                        flag = isSubjectMatch(i, j+1, s, p)
            else:
                flag = False
        else:
            if j < len(p):
                flag = isPCouldNone(j, p)
            else:
                flag = True
        return flag

    p_stack = generatePStack(p)
    p_stack = removePSameItem(p_stack)
    print(p_stack)
    return isSubjectMatch(0, 0, s, p_stack)

if __name__ == "__main__":
    s = "abcbccbcbaabbcbb"
    p = "c*a.*ab*.*ab*a*..b*"
    start_time = time.time()
    result = isMatch(s, p)
    print("用时：", round(time.time()-start_time,2))
    print(result)