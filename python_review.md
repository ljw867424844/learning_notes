### Python基础

##### 1. 缩进

Python 使用缩进来组织代码块，请务必遵守约定俗成的习惯，坚持使用 **4 个空格** 的缩进； 在文本编辑器中，需要设置把 Tab 自动转换为 4 个空格，确保不混用 Tab 和空格。

##### 2. 数据类型和变量

由于整数和浮点数在计算机内部存储方式的不同，整数运算永远是精确的，而浮点数运算则可能会有四舍五入的误差。例如：

```python
>>> 1 + 2
3
>>> 0.1 + 0.2
0.30000000000000004
```

等号 `=` 是赋值语句，可以把任意数据类型赋值给变量，同一个变量可以反复赋值，而且可以是不同类型的变量。这种变量本身类型不固定的语言称之为 **动态语言**，与之对应的是 **静态语言**。静态语言在定义变量时必须指定变量类型，如果赋值的时候类型不匹配，就会报错。例如 Java 是静态语言。

Python 的整数没有大小限制，而某些语言的整数根据其存储长度是有大小限制的，例如 Java 对 32 位整数的范围限制在 -2147483648 - 2147483647 。Python 的浮点数也没有大小限制，但是超出一定范围就直接表示为 inf （无限大）。

##### 3. 字符串和编码

由于计算机是美国人发明的，因此，最早只有 127 个字符被编码到计算机里，也就是大小写英文字母、数字和一些符号，这个编码表被称为 **ASCII 编码** ，比如大写字母 A 的编码是 65，小写字母 z 的编码是 122。

全世界有上百种语言，日本把日文编到 Shift_JIS 里，韩国把韩文编到 Euc-kr 里，各国有各国的标准，就会不可避免地出现冲突，结果就是，在多语言混合的文本中，显示出来会有乱码。 因此， **Unicode 字符集** 应运而生。Unicode 把所有语言都统一到一套编码里，这样就不会再有乱码问题了。

如果统一成 Unicode 编码，乱码问题从此消失了。但是，如果你写的文本基本上全部是英文的话，用Unicode 编码比 ASCII 编码需要多一倍的存储空间，在存储和传输上就十分不划算。 所以，本着节约的精神，又出现了把 Unicode 编码转化为“可变长编码”的 **UTF-8 编码** 。UTF-8 编码把一个 Unicode 字符根据不同的数字大小编码成 1 - 6 个字节，常用的英文字母被编码成 1 个字节，汉字通常是 3 个字节，只有很生僻的字符才会被编码成 4 - 6 个字节。如果你要传输的文本包含大量英文字符，用 UTF-8 编码就能节省空间。

对于单个字符的编码，Python 提供了 `ord()` 函数获取字符的整数表示，`chr()` 函数把编码转换为对应的字符。

```python
>>> ord('A')
65
>>> ord('中')
20013
>>> chr(66)
'B'
>>> chr(25991)
'文'
```

当 str 和 bytes 互相转换时，需要指定编码。最常用的编码是 UTF-8。

以 Unicode 表示的 str 通过 `encode()` 方法可以编码为指定的 bytes，例如：

```python
>>> 'ABC'.encode('ascii')
b'ABC'
>>> '中文'.encode('utf-8')
b'\xe4\xb8\xad\xe6\x96\x87'
>>> '中文'.encode('ascii')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-1:
ordinal not in range(128)
```

反过来，如果我们从网络或磁盘上读取了字节流，那么读到的数据就是 bytes。要把 bytes 变为 str，就需要用 `decode()` 方法：

```python
>>> b'ABC'.decode('ascii')
'ABC'
>>> b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
'中文'
>>> b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore')
'中'
```

`len()` 函数计算的是 str 的字符数，如果换成 bytes， `len()` 函数就计算字节数:

```python
>>> len('ABC')
3
>>> len('中文')
2
>>> len(b'ABC')
3
>>> len(b'\xe4\xb8\xad\xe6\x96\x87')
6
>>> len('中文'.encode('utf-8'))
6
```

##### 4. 使用 list 和 tuple

把元素插入到指定的位置，用 `insert()` 方法，比如插入到索引号为 1 的位置：

```python
>>> classmates.insert(1, 'Jack')
>>> classmates
['Michael', 'Jack', 'Bob', 'Tracy', 'Adam']
```

删除 list 末尾的元素，用 `pop()` 方法（有返回值）

```python
>>> classmates.pop()
'Adam'
>>> classmates
['Michael', 'Jack', 'Bob', 'Tracy']
```

要删除指定位置的元素，用 `pop(i)` 方法，其中 i 是索引位置：

```python
>>> classmates.pop(1)
'Jack'
>>> classmates
['Michael', 'Bob', 'Tracy']
```

tuple 所谓的“不变”是说，tuple 的每个元素，**指向** 永远不变。但这个元素如果可变则可变。

```python
>>> t = ('a', 'b', ['A', 'B'])
>>> t[2][0] = 'X'
>>> t[2][1] = 'Y'
>>> t
('a', 'b', ['X', 'Y'])
```

##### 5. 条件判断

当我们用 `if ... elif ... elif ... else ...` 判断时，会写很长一串代码，可读性较差。 如果要针对某个变量匹配若干种情况，可以使用 match 语句:

```python
score = 'B'
match score:
    case 'A':
		print('score is A.')
    case 'B':
 		print('score is B.')
 	case 'C':
 		print('score is C.')
 	case _: # _表示匹配到其他任何情况
 		print('score is ???.')
```

##### 6. 使用 dict 和 set

dict 可以用在需要高速查找的很多地方，在 Python 代码中几乎无处不在，正确使用 dict 非常重要，需要牢记的第一条就是 **dict 的 key 必须是不可变对象** 。这是因为 dict 根据 key 来计算 value 的存储位置，如果每次计算相同的 key 得出的结果不同，那 dict 内部就完全混乱了。这个通过 key 计算位置的算法称为 **哈希算法（Hash）**。 要保证 hash 的正确性，作为 key 的对象就不能变。在 Python 中，字符串、整数等都是不可变的，因此，可以放心地作为 key。而 list 是可变的，就不能作为 key。

set 和 dict 的唯一区别仅在于没有存储对应的 value。但是，set 的原理和 dict 一样，故同样不可以放入可变对象。因为无法判断两个可变对象是否相等，也就无法保证 set 内部“不会有重复元素”。

对于不变对象来说，调用对象自身的任意方法，也不会改变该对象自身的内容。相反，这些方法会创建新的对象并返回，这样，就保证了 **不可变对象本身永远是不可变的**。

```python
>>> a = 'abc'
>>> b = a.replace('a', 'A')
>>> b
'Abc'
>>> a
'abc
```

### 函数

##### 1. 函数的参数

- 位置参数。最常见的参数，按顺序传递。

- 关键字参数。调用时用 ` 参数名=值` 的形式传递，顺序可以不固定。

- 默认参数。在定义函数时给参数设置默认值，调用时可省略。默认参数必须指向不可变对象！

- 可变位置参数。用 ` *` 收集任意个位置参数，传入函数时会打包成 tuple。 

- 可变关键字参数。用 ` **` 收集任意个关键字参数，传入函数时会打包成 dict。

- 仅限位置参数。在参数列表中使用 `/` 之前的参数必须用位置传递。

- 仅限关键字参数。在参数列表中使用 `*` 之后的参数必须用关键字传递。

##### 2. 递归函数

使用递归函数需要注意防止 **栈溢出**。在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。

普通递归（阶乘）：

```python
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)  # 递归调用后，还要再乘 n
```

解决递归调用栈溢出的方法是通过 **尾递归** 优化。尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。

尾递归版本（阶乘）：

```python
def fact_tail(n, acc=1):
    if n == 1:
        return acc
    return fact_tail(n - 1, n * acc)  # 最后一步就是调用自身
```



使用递归函数的优点是逻辑简单清晰，缺点是过深的调用会导致栈溢出。

### 高级特性

##### 1. 切片

在 Python 里，**切片（slice）** 是一种从 **序列（sequence）类型对象**（比如 `list` 、 `tuple` 、 `str`）中，按指定范围提取子序列的操作。他的基本语法是：

```python
sequence[start:stop:step]
```

参数说明：
- `start`：切片的起始索引（包含），默认是 `0`。
- `stop`：切片的结束索引（不包含），默认是序列的长度。
- `step`：切片的步长（默认为 `1`）。

其特点为：
- 不会修改原序列，而是返回一个新的序列。
- 支持负索引。
- 灵活性很高，常用于反转、跳步取值、截取子串。

##### 2. 迭代

通过 **for 循环** 来依次访问可迭代对象里的元素，直到结束。这种遍历我们称为 **迭代**。

为什么要迭代？

- 代码简洁：不用手动处理下标。
- 节省内存：像生成器那样惰性迭代。
- 统一接口：不同类型（list、tuple、set）都可以用同样的 `for` 遍历。

##### 3. 列表推导式

作用：用一行语句快速创建列表。

语法：

```python
[expression for item in iterable if condition]
```

- `expression`：生成元素的表达式
- `item`：可迭代对象中的元素
- `condition`：筛选条件（可选）

缺点：一次性创建完整列表，占用内存

##### 4. 迭代器

可以直接作用于 for 循环的对象统称为 **可迭代对象（Iterable）**。 可以使用 `isinstance()` 判断一个对象是否是 Iterable 对象：

```python
>>> from collections.abc import Iterable
>>> isinstance([], Iterable)
True
>>> isinstance({}, Iterable)
True
>>> isinstance('abc', Iterable)
True
>>> isinstance((x for x in range(10)), Iterable)
True
>>> isinstance(100, Iterable)
False
```

可以被 `next()` 函数调用并不断返回下一个值的对象称为 **迭代器（Iterator）**。 可以使用 `isinstance() `判断一个对象是否是 Iterator 对象：

```python
>>> from collections.abc import Iterator
>>> isinstance((x for x in range(10)), Iterator)
True
>>> isinstance([], Iterator)
False
>>> isinstance({}, Iterator)
False
>>> isinstance('abc', Iterator)
False
```

list、dict、str 虽然是可迭代对象，却不是迭代器。 把 list、dict、str 等可迭代对象变成迭代器可以使用 `iter()` 函数：

```python
>>> isinstance(iter([]), Iterator)
True
>>> isinstance(iter('abc'), Iterator)
True
```

##### 5. 生成器

生成器（generator）是一种特殊的迭代器，它可以在需要时“惰性”地产生值，而不是一次性把所有数据放到内存里。这样做有两个主要好处：

- **节省内存**（不需要存储整个序列）

- **提高效率**（按需计算）

要创建一个 generator，有很多种方法。第一种方法很简单，使用 **生成器表达式**。只要把一个列表推导式的 `[]` 改成` ()` ，就创建了一个 generator。

```python
>>> L = [x * x for x in range(5)]
>>> L
[0, 1, 4, 9, 16]
>>> g = (x * x for x in range(5))
>>> g
<generator object <genexpr> at 0x1022ef630>
```

通过 `next()` 函数获得 generator 的下一个返回值:

```python
>>> next(g)
0
>>> next(g)
1
>>> next(g)
4
>>> next(g)
9
>>> next(g)
16
>>> next(g)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

generator 保存的是算法，每次调用 `next(g)` ，就计算出 `g` 的下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出 **StopIteration** 的错误。

第二种方法为使用 **生成器函数** 。如果一个函数定义中包含 `yield` 关键字，那么这个函数就不再是一个普通函数，而是一个生成器函数。调用一个生成器函数将返回一个生成器：

```python
def fib(max):
    n, a, b = 0, 0, 1
	while n < max:
		yield b
 		a, b = b, a + b
 		n = n + 1
	return 'done'
```

```python
>>> f = fib(6)
>>> f
<generator object fib at 0x104feaaa0>
```

普通函数用 `return` 返回值后就结束了，而生成器函数在 `yield` 时会“暂停”，下次再调用时继续从上一次暂停的位置执行。因此，生成器 **不会一次性把所有数据存入内存**，而是 **按需（惰性）生成数据**。

把函数改成 generator 函数后，我们基本上从来不会用 `next()` 来获取下一个返回值， 而是直接使用 for 循环来迭代。

但是用 for 循环调用 generator 时，发现拿不到 generator 的 return 语句的返回值。如果想要拿到返回值，必须捕获 StopIteration 错误，返回值包含在 StopIteration 的 value 中。

```python
>>> g = fib(6)
>>> while True:
... 	try:
... 		x = next(g)
... 		print('g:', x)
... 	except StopIteration as e:
... 		print(e.value)
... 	break
...
g: 1
g: 1
g: 2
g: 3
g: 5
g: 8
done
```

### 高阶函数

##### 1. map

`map(func, iterable)`

对序列中的每个元素应用函数，返回迭代器。

ps：**序列一定是可迭代对象**，但并不是所有可迭代对象都是序列（例如：集合 `set`、字典 `dict` 也是可迭代的，但它们不是序列，因为无序、不能用下标取值）

```python
nums = [1, 2, 3, 4]
print(list(map(lambda x: x*2, nums)))  # [2, 4, 6, 8]
```

##### 2. reduce

`reduce(func, iterable[, initializer])`

把序列“累积”成一个结果。

```python
from functools import reduce
nums = [1, 2, 3, 4]
print(reduce(lambda x, y: x+y, nums))  # 10
```

##### 3. filter

`filter(func, iterable)`

用函数过滤序列，保留返回值为 True 的元素。

```python
nums = [1, 2, 3, 4, 5]
print(list(filter(lambda x: x % 2 == 0, nums)))  # [2, 4]
```

##### 4. sorted

`sorted(iterable, key=func, reverse=False)`

通过 `key` 函数自定义排序规则。

```python
print(sorted(["apple", "watermelon", "cherry"], key=len))  
# ['apple', 'cherry', 'watermelon']
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))  
# ['Zoo', 'Credit', 'bob', 'about']
```

##### 5. 返回函数

高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。

- 核心机制：依赖于 **闭包**（返回的函数会记住外层变量）。

- 应用场景：函数工厂、延迟执行、装饰器等。

函数工厂：

```python
def power(exp):
    def inner(x):
        return x ** exp
    return inner

square = power(2)  # 返回一个平方函数
cube = power(3)    # 返回一个立方函数

print(square(5))  # 25
print(cube(2))    # 8
```

`power` 返回的函数 `inner` 记住了外部变量 `exp`，这就是 **闭包**。

延迟计算：

```python
def make_adder(x):
    def adder(y):
        return x + y
    return adder

add5 = make_adder(5)
print(add5(10))  # 15
```

返回的函数 `adder` 在需要的时候才执行。

用于装饰器：

```python
def log(func):
    def wrapper(*args, **kwargs):
        print(f"调用函数 {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log
def hello():
    print("Hello")

hello()
```

`log` 返回了 `wrapper`，替代了原始函数。

**6. 装饰器**

在代码运行期间动态增加功能的方式，称之为“装饰器”。它的核心是：在不改动原函数的前提下，统一修改调用行为

```python
def log(func):
    def wrapper(*args, **kwargs):
        print(f"[前置] 即将调用 {func.__name__}")
        result = func(*args, **kwargs)
        print(f"[后置] {func.__name__} 调用完毕")
        return result
    return wrapper

@log
def hello(person):
    print(f"Hello,{person}")

hello('Jiawen Li')
```

```python
[前置] 即将调用 hello
Hello,Jiawen Li
[后置] hello 调用完毕
```

ps：**语法糖（Syntactic Sugar）** 是编程语言里提供的一种写法，它不会增加新功能，只是让代码 更简洁、更易读。换句话说：“语法糖”就是把一段常用的写法，换一种 **更甜、更顺手** 的写法。

- 装饰器语法糖

```python
@log
def hello():
    print("Hello")
```

等价于：

```python
def hello():
    print("Hello")
hello = log(hello)
```

`@log` 就是语法糖 —— 少写一行 `hello = log(hello)`。

- 列表推导式

`squares = [x*x for x in range(5)]` 等价于：

```python
squares = []
for x in range(5):
    squares.append(x*x)
```

列表推导式就是 for 循环的语法糖。

- `with` 上下文管理

```python
with open("data.txt") as f:
    content = f.read()
```

等价于：

```python
f = open("data.txt")
try:
    content = f.read()
finally:
    f.close()
```

`with` 就是 try/finally 的语法糖。
