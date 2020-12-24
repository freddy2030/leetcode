"""
超时
"""
def canReorderDoubled(A) -> bool:
    flag = True
    A.sort()
    while len(A)>0:
        a = A.pop()
        if (a<0) & flag:
            A.append(a)
            A.sort(reverse=True)
            continue
        if a/2 in A:
            A.remove(a/2)
        else:
            return False
    return True

def canReorderDoubled1(A) -> bool:
    m = {}
    for i in A:
        if i in m.keys():
            m[i] += 1
        else:
            m[i] = 1
    keys = list(m.keys())
    keys.sort()
    for i in keys:
        if i > 0:
            g = 2
        else:
            g = 1/2
        if m[i] == 0:
            continue

        if i*g in keys:
            if m[i] <= m[i*g]:
                m[i*g] -= m[i]
            else:
                return False
        else:
            return False
    return True

if __name__ == "__main__":
    A = [4,-2,2,-4]
    result = canReorderDoubled1(A)
    print(result)