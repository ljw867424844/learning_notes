def move(n, a, b, c):
    """
    汉诺塔问题的递归解决方案
    
    参数:
        n: 盘子的数量
        a: 起始柱子
        b: 辅助柱子
        c: 目标柱子
    """
    if n == 1:
        print(a, '-->', c)
    else:
        # 将n-1个盘子从a借助c移动到b
        move(n-1, a, c, b)
        
        # 将最大的盘子从a移动到c
        print(a, '-->', c)
        
        # 将n-1个盘子从b借助a移动到c
        move(n-1, b, a, c)

# 测试代码
move(3, 'A', 'B', 'C')
