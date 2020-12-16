def longestValidParentheses(s: str) -> int:
    s = list(s)
    dp = []
    for i, v in enumerate(s):
        if v == "(":
            dp.append(i)
        else:
            if len(dp) != 0:
                j = dp.pop()
                s[j] = 0
                s[i] = 0
    r = 0
    max_r = 0
    for i in s:
        if i == 0:
            r += 1
            max_r = max(max_r, r)
        else:
            r = 0
    return max_r

if __name__ == "__main__":
    s = "()(()"
    result = longestValidParentheses(s)
    print(result)