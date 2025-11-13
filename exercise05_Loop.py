"""
练习1：请利用循环依次对list中的每个名字打印出Hello, xxx!：

L = ['Bart', 'Lisa', 'Adam']
for x in L:
    print('Hello, x!')

"""
"""
练习2：打印100以内的奇数，2除外，若为合数则退出。

def is_composite(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return True
    return False

for i in range(1,101):
    if i %2 != 0:
        if is_composite(i) :
            break
        else:
            print(i)
"""
"""
练习3：

while True:
    num = int(input("请输入一个整数（输入负数退出）："))
    if num < 0:
        print("输入了负数，程序结束。")
        break
    if num == 0:
        print("输入的是 0，跳过。")
        continue
    print(f"你输入的平方是：{num ** 2}")

"""

