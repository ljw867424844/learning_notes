def mul(*num):
    if not num:
        raise TypeError
    result = 1
    for n in num:
        result *= n
    return result

# 测试
assert mul(0) == 0
assert mul(5) == 5
assert mul(5, 6) == 30
assert mul(5, 6, 7) == 210
assert mul(5, 6, 7, 9) == 1890

try:
    mul()
    print('mul()测试失败!')
except TypeError:
    print('OK')


