def trim(s):
    """
    利用切片操作，实现一个trim()函数，去除字符串首尾的空格，
    注意不要调用str的strip()方法：
    """
    # 去掉开头的空格
    while len(s) > 0 and s[0] == ' ':
        s = s[1:]
    # 去掉结尾的空格
    while len(s) > 0 and s[-1] == ' ':
        s = s[:-1]
    return s

# 测试:
assert trim('hello  ') == 'hello'
assert trim('  hello') == 'hello'
assert trim('  hello  ') == 'hello'
assert trim('  hello  world  ') == 'hello  world'
assert trim('') == ''
assert trim('    ') == ''

print('测试成功!')
