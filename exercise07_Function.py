"""
1.请利用Python内置的hex()函数把一个整数转换成十六进制表示的字符串：
def ten_2_sixteen(n):
	print(f'{n}的十六进制为{hex(n)}')

n1 = 255
n2 = 1000

ten_2_sixteen(n1)
ten_2_sixteen(n2)

"""
"""
2.请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程的两个解。
"""
import math

def quadratic(a, b, c):
    delta = b*b - 4*a*c
    if delta < 0:
        return None
    elif delta == 0:
        x = -b / (2*a)
        return x
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return x1, x2

# 测试:
print('quadratic(1, 2, 5) =', quadratic(1, 2, 5))
print('quadratic(1, 2, 1) =', quadratic(1, 2, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

assert quadratic(1, 2, 5) == None
assert quadratic(1, 2, 1) == -1
assert quadratic(1, 3, -4) == (1.0, -4.0)

print('OK')

