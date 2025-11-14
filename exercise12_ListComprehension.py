"""使用列表推导式"""
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [x.lower() for x in L1 if isinstance(x, str)]
L3 = [x.lower() if isinstance(x, str) else x for x in L1]

# 测试:
print(L2)
print(L3)
assert L2 == ['hello', 'world', 'apple']
assert L3 == ['hello', 'world', 18, 'apple', None]

print('OK!')

