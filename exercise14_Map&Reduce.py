"""
1.利用map()函数，
把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。

def normalize(name):
    return name[0].upper() + name[1:].lower()

L1 = ['','adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)
"""
"""
2.Python提供的sum()函数可以接受一个list并求和，
请编写一个prod()函数，可以接受一个list并利用reduce()求积：

from functools import reduce

def prod(L):
    return reduce(lambda x, y: x * y, L)

print('3 + 5 + 7 + 9 =', sum([3, 5, 7, 9]))
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
assert prod([3, 5, 7, 9]) == 945
print('OK!')
"""
"""
3.利用map和reduce编写一个str2float函数，
把字符串'123.456'转换成浮点数123.456：
"""
from functools import reduce

def str2float(s):
    # 划分成'123'和'456'
    left_str, right_str = s.split('.')

    # 将字符转为整数
    def char2num(c):
        return ord(c) - ord('0')

    # 计算整数部分的数值
    left_value = reduce(lambda x, y: x * 10 + y, map(char2num, left_str))

    # 计算小数部分的数值
    right_value = reduce(lambda x, y: x * 10 + y, map(char2num, right_str)) / (10 **len(right_str))
    
    return left_value + right_value

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:   # 浮点数计算可能有微小误差
    print('测试成功!')
else:
    print('测试失败!')

