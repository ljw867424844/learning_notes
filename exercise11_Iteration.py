"""
请使用迭代查找一个list中最小和最大值，并返回一个tuple：
"""
def findMinAndMax(L):
    if not L:
        return None, None
    
    min = L[0]
    max = L[0] 

    for x in L:
        if x < min:
            min = x
        if x > max:
            max = x

    return min, max

# 测试
assert findMinAndMax([]) == (None, None)
assert findMinAndMax([7]) == (7, 7)
assert findMinAndMax([7, 1]) == (1, 7)
assert findMinAndMax([7, 1, 3, 9, 5]) == (1, 9)

print('OK!')
