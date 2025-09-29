### Python基础

##### 1. 缩进

Python使用缩进来组织代码块，请务必遵守约定俗成的习惯，坚持使用 **4 个空格** 的缩进； 在文本编辑器中，需要设置把Tab自动转换为4个空格，确保不混用Tab和空格。

##### 2. 数据类型和变量

由于整数和浮点数在计算机内部存储方式的不同，整数运算永远是精确的，而浮点数运算则可能会有四舍五入的误差。例如：

```python
>>> 1 + 2
3
>>> 0.1 + 0.2
0.30000000000000004
```

等号 `=` 是赋值语句，可以把任意数据类型赋值给变量，同一个变量可以反复赋值，而且可以是不同类型的变量。这种变量本身类型不固定的语言称之为 **动态语言**，与之对应的是 **静态语言**。静态语言在定义变量时必须指定变量类型，如果赋值的时候类型不匹配，就会报错。例如Java是静态语言。

Python的整数没有大小限制，而某些语言的整数根据其存储长度是有大小限制的，例如Java对32位整数的范围限制在-2147483648 - 2147483647。Python的浮点数也没有大小限制，但是超出一定范围就直接表示为inf（无限大）。

##### 3. 字符串和编码

由于计算机是美国人发明的，因此，最早只有127个字符被编码到计算机里，也就是大小写英文字母、数字和一些符号，这个编码表被称为 **ASCII 编码** ，比如大写字母A的编码是65，小写字母z的编码是122。

全世界有上百种语言，日本把日文编到Shift_JIS里，韩国把韩文编到Euc-kr里，各国有各国的标准，就会不可避免地出现冲突，结果就是，在多语言混合的文本中，显示出来会有乱码。 因此， **Unicode 字符集** 应运而生。Unicode 把所有语言都统一到一套编码里，这样就不会再有乱码问题了。

如果统一成Unicode编码，乱码问题从此消失了。但是，如果你写的文本基本上全部是英文的话，用Unicode编码比ASCII编码需要多一倍的存储空间，在存储和传输上就十分不划算。 所以，本着节约的精神，又出现了把Unicode编码转化为“可变长编码”的 **UTF-8 编码** 。UTF-8编码把一个Unicode字符根据不同的数字大小编码成1-6个字节，常用的英文字母被编码成1个字节，汉字通常是3个字节，只有很生僻的字符才会被编码成4-6个字节。如果你要传输的文本包含大量英文字符，用UTF-8编码就能节省空间。

对于单个字符的编码，Python提供了 `ord()` 函数获取字符的整数表示，`chr()` 函数把编码转换为对应的字符。

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

当str和bytes互相转换时，需要指定编码。最常用的编码是UTF-8。

以Unicode表示的str通过 `encode()` 方法可以编码为指定的bytes，例如：

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

反过来，如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用 `decode()` 方法：

```python
>>> b'ABC'.decode('ascii')
'ABC'
>>> b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
'中文'
>>> b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore')
'中'
```

`len()` 函数计算的是str的字符数，如果换成bytes， `len()` 函数就计算字节数:

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

##### 4. 使用list和tuple

把元素插入到指定的位置，用 `insert()` 方法，比如插入到索引号为1的位置：

```python
>>> classmates.insert(1, 'Jack')
>>> classmates
['Michael', 'Jack', 'Bob', 'Tracy', 'Adam']
```

删除list末尾的元素，用 `pop()` 方法（有返回值）

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

tuple所谓的“不变”是说，tuple的每个元素，**指向** 永远不变。但这个元素如果可变则可变。

```python
>>> t = ('a', 'b', ['A', 'B'])
>>> t[2][0] = 'X'
>>> t[2][1] = 'Y'
>>> t
('a', 'b', ['X', 'Y'])
```

##### 5. 条件判断

当我们用 `if ... elif ... elif ... else ...` 判断时，会写很长一串代码，可读性较差。 如果要针对某个变量匹配若干种情况，可以使用match语句:

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

##### 6. 使用dict和set

dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，正确使用dict非常重要，需要牢记的第一条就是 **dict 的 key 必须是不可变对象** 。这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。这个通过key计算位置的算法称为 **哈希算法（Hash）**。 要保证hash的正确性，作为key的对象就不能变。在Python中，字符串、整数等都是不可变的，因此，可以放心地作为 key。而list是可变的，就不能作为key。

set和dict的唯一区别仅在于没有存储对应的value。但是，set的原理和dict 一样，故同样不可以放入可变对象。因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”。

对于不可变对象来说，调用对象自身的任意方法，也不会改变该对象自身的内容。相反，这些方法会创建新的对象并返回，这样，就保证了 **不可变对象本身永远是不可变的**。

```python
>>> a = 'abc'
>>> b = a.replace('a', 'A')
>>> b
'Abc'
>>> a
'abc
```

### 函数

##### 1. 调用函数

Python内置了很多有用的函数，我们可以直接调用。

调用函数的时候，如果传入的参数数量不对，会报 `TypeError` 的错误，并且Python会明确地告 诉你： `abs()` 有且仅有1个参数，但给出了两个：

```python
>>> abs(1, 2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: abs() takes exactly one argument (2 given)
```

如果传入的参数数量是对的，但参数类型不能被函数所接受，也会报 `TypeError` 的错误，并且 给出错误信息：

```python
>>> abs('a')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: bad operand type for abs(): 'str'
```

##### 2. 定义函数

定义函数时，需要确定函数名和参数个数；如果有必要，可以先对参数的数据类型做检查；

函数体内部的语句在执行时，一旦执行到 `return` 时，函数就执行完毕，并将结果返回。因此，函数内部通过条件判断和循环可以实现非常复杂的逻辑。

如果没有 `return` 语句，函数执行完毕后也会返回结果，只是结果为 `None` 。 `return None` 可以简写为 `return` 。

函数可以返回多个值，返回值是一个tuple！但是，在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值，所以，Python的函数返回多值其实就是返回一个tuple， 但写起来更方便。

##### 3. 函数的参数

- 位置参数。最常见的参数，按顺序传递。

- 关键字参数。调用时用 ` 参数名=值` 的形式传递，顺序可以不固定。

- 默认参数。在定义函数时给参数设置默认值，调用时可省略。默认参数必须指向不可变对象！

- 可变位置参数。用 ` *` 收集任意个位置参数，传入函数时会打包成tuple。 

- 可变关键字参数。用 ` **` 收集任意个关键字参数，传入函数时会打包成dict。

- 仅限位置参数。在参数列表中使用 `/` 之前的参数必须用位置传递。

- 仅限关键字参数。在参数列表中使用 `*` 之后的参数必须用关键字传递。

##### 4. 递归函数

使用递归函数需要注意防止 **栈溢出**。在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。

普通递归（阶乘）：

```python
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)  # 递归调用后，还要再乘n
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

在Python里，**切片（slice）** 是一种从 **序列（sequence）类型对象**（比如 `list` 、 `tuple` 、 `str`）中，按指定范围提取子序列的操作。他的基本语法是：

```python
sequence[start:stop:step]
```

参数说明：

- `start`：切片的起始索引（包含），默认是0。
- `stop`：切片的结束索引（不包含），默认是序列的长度。
- `step`：切片的步长（默认为1。

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

可以直接作用于 for 循环的对象统称为可迭代对象（Iterable）。 可以使用 `isinstance()` 判断一个对象是否是可迭代对象：

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

可以被 `next()` 函数调用并不断返回下一个值的对象称为 **迭代器（Iterator）**。 可以使用 `isinstance() `判断一个对象是否是迭代器：

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

list、dict、str虽然是可迭代对象，却不是迭代器。 把list、dict、str等可迭代对象变成迭代器可以使用 `iter()` 函数：

```python
>>> isinstance(iter([]), Iterator)
True
>>> isinstance(iter('abc'), Iterator)
True
```

##### 5. 生成器

生成器（generator）是一种特殊的迭代器。

要创建一个generator，有很多种方法。第一种方法很简单，使用 **生成器表达式**。只要把一个列表推导式的 `[]` 改成` ()` ，就创建了一个generator。

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

generator保存的是算法，每次调用 `next(g)` ，就计算出 `g` 的下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出 **StopIteration** 的错误。

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

普通函数用 `return` 返回值后就结束了，而生成器函数在 `yield` 时会“暂停”，下次再调用时继续从上一次暂停的位置执行。

| 特性     | 迭代器 (Iterator)                   | 生成器 (Generator)                            |
| -------- | ----------------------------------- | --------------------------------------------- |
| 定义方式 | 写类，定义 `__iter__` 和 `__next__` | 函数里用 `yield` 或生成器表达式               |
| 本质     | 遵循迭代器协议的对象                | 特殊的迭代器（语法糖）                        |
| 使用难度 | 繁琐，要维护状态                    | 简洁，Python 自动维护状态                     |
| 功能     | 只能 `next()`                       | 支持 `next()`、`send()`、`throw()`、`close()` |
| 适用场景 | 复杂迭代逻辑，面向对象封装          | 流式数据、简单顺序逻辑、协程                  |

### 函数式编程

##### 1. 函数作为参数

- map函数

`map(func, iterable)`

对序列中的每个元素应用函数，返回迭代器。

ps：**序列一定是可迭代对象**，但并不是所有可迭代对象都是序列（例如：集合 `set`、字典 `dict` 是可迭代对象，但它们不是序列，因为无序且不能用下标取值）

```python
nums = [1, 2, 3, 4]
print(list(map(lambda x: x*2, nums)))  # [2, 4, 6, 8]
```

- reduce函数

`reduce(func, iterable[, initializer])`

把序列“累积”成一个结果。

```python
from functools import reduce
nums = [1, 2, 3, 4]
print(reduce(lambda x, y: x+y, nums))  # 10
```

- filter函数

`filter(func, iterable)`

用函数过滤序列，保留返回值为True的元素。

```python
nums = [1, 2, 3, 4, 5]
print(list(filter(lambda x: x % 2 == 0, nums)))  # [2, 4]
```

- sorted函数

`sorted(iterable, key=func, reverse=False)`

通过 `key` 函数自定义排序规则。

```python
print(sorted(["apple", "watermelon", "cherry"], key=len))  
# ['apple', 'cherry', 'watermelon']
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))  
# ['Zoo', 'Credit', 'bob', 'about']
```

##### 2. 返回函数

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

##### 3. 装饰器

在代码运行期间动态增加功能的方式，称之为“装饰器”。它的核心是：在不改动原函数的前提下，统一修改调用行为：

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

列表推导式就是for循环的语法糖。

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

`with` 就是try/finally的语法糖。

### 面向对象编程

##### 1. 类和实例

类是创建实例的模板，而实例则是一个一个具体的对象，各个实例拥有的数据都互相独立，互不影响；

方法就是与实例绑定的函数，和普通函数不同，方法可以直接访问实例的数据；

通过在实例上调用方法，我们就直接操作了对象内部的数据，但无需知道方法内部的实现细节。

值得注意的是，在Python里，对象的实例变量 **不需要预先声明类型**，也 **不受限制**，你可以随时给它赋值，不管是数字、字符串、列表，甚至函数、类都可以。简而言之，你可以**在运行时随时往对象里加属性，并赋予它任何数据**。

```python
class Demo:
    pass

d = Demo()

# 动态绑定实例变量
d.x = 10          # 绑定整数
d.y = "hello"     # 绑定字符串
d.z = [1, 2, 3]   # 绑定列表
d.func = lambda a, b: a + b   # 绑定函数

print(d.x)        # 10
print(d.y)        # hello
print(d.z)        # [1, 2, 3]
print(d.func(2,3)) # 5
```

##### 2. 访问限制

如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线 __ ，在Python中，实例的变量名如果以 __ 开头，就变成了一个 **私有变量（private）**，只有内部可以访问，外部不能访问。这样就确保了外部代码不能随意修改对象内部的状态，这样通过访问限制的保护，代码更加健壮。

```python
class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score
        
    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))
```

```python
>>> bart = Student('Bart Simpson', 59)
>>> bart.__name
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Student' object has no attribute '__name'
```

但是，如果外部代码要获取甚至修改 `name` 怎么办？此时，可以给Student类增加 `get_name` 和 `set_score` 这样的方法。

```python
def get_name(self):
    return self.__name
def set_name(self,name):
    self.__name = name
```

##### 3. 继承和多态

继承可以把父类的所有功能都直接拿过来，这样就不必从零做起，子类只需要新增自己特有的方法，也可以把父类不适合的方法覆盖重写。

对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，否则，将无法调用 `run()` 方法。 对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个 `run()` 方法就可以了：

```python
def Timer():
    def run(self):
        print('Start...')
```

这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，是一种“按行为来认定类型”的方式。一个对象只要“看起来像鸭子，走起 路来像鸭子”，那它就可以被看做是鸭子。

##### 4. 获取对象信息

- 使用 `Type()` 函数

基本类型都可以用 `type()` 判断，如果一个变量指向函数或者类，也可以用 `type()` 判断。

```python
>>> type(123)
<class 'int'>
>>> type('str')
<class 'str'>
>>> type(None)
<type(None) 'NoneType'>
>>> type(abs)
<class 'builtin_function_or_method'>
>>> type(a)
<class '__main__.Animal'>
```

- 使用 `isinstance()` 函数

`isinstance()` 判断的是一个对象是否是该类型本身，或者位于该类型的父继承链上。

```python
>>> a = Animal()
>>> d = Dog()
>>> h = Husky()
>>> isinstance(h, Husky)
True
>>> isinstance(h, Dog)
True
>>> isinstance(h, Animal)
True
>>> isinstance(d, Husky)
False
```

能用 `type()` 判断的基本类型也可以用 `isinstance()` 判断。

```python
>>> isinstance('a', str)
True
>>> isinstance(123, int)
True
>>> isinstance(b'a', bytes)
True
```

并且还可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是list或者tuple。

```python
>>> isinstance([1, 2, 3], (list, tuple))
True
>>> isinstance((1, 2, 3), (list, tuple))
True
```

- 使用 `dir()` 函数

使用 `dir()` 函数，可以获得一个对象的所有属性和方法，它返回一个包含字符串的list。

```python
>>> dir('ABCDEFG')
['__add__', '__class__',..., '__subclasshook__', 'capitalize','casefold',..., 'zfill']
```

类似 `__xxx__` 的属性和方法在Python中都是有特殊用途的，比如 `__len__` 方法返回长度。在Python中，如果你调用 `len()` 函数试图获取一个对象的长度，实际上，在 `len()` 函数内部， 它自动去调用该对象的 `__len__()` 方法，所以，下面的代码是等价的：

```python
>>> len('ABC')
3
>>> 'ABC'.__len__()
3
```

##### 5. 示例属性和类属性

由于Python是动态语言，根据类创建的示例可以任意绑定属性。

**给实例绑定属性** 的方法是通过实例变量（前面已演示），或者通过self变量，如下：

```python
class Student(object):
    def __init__(self, name):
        self.name = name

s = Student('Bob')
```

但是，如果Student类本身需要绑定一个属性呢？可以直接在class中定义属性，这种属性是类属性，归Student类所有：

```python
class Student(object):
    name = 'Student'
```

当我们定义了一个类属性后，这个属性虽然归类所有，但类的所有实例都可以访问到。来测试一 下：

```python
>>> class Student(object):
...     name = 'Student'
...
>>> s = Student() # 创建实例s
>>> print(s.name) # 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性
Student
>>> print(Student.name) # 打印类的name属性
Student
>>> s.name = 'Michael' # 给实例绑定name属性
>>> print(s.name) # 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
Michael
>>> print(Student.name) # 但是类属性并未消失，用Student.name仍然可以访问
Student
>>> del s.name # 如果删除实例的name属性
>>> print(s.name) # 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了
Student
```

实例属性属于各个实例所有，互不干扰； 类属性属于类所有，所有实例共享一个属性；

不要对实例属性和类属性使用相同的名字，否则将产生难以发现的错误。

### 面向对象高级编程

##### 1. 使用 `__slots__`

Python允许在定义class的时候，定义一个特殊的 `__slots__` 变量， 来限制该class实例能添加的属性：

```python
class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称
```

然后，可以试一试：

```python
>>> s = Student() # 创建新的实例
>>> s.name = 'Michael' # 绑定属性'name'
>>> s.age = 25 # 绑定属性'age'
>>> s.score = 99 # 绑定属性'score'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Student' object has no attribute 'score'
```

使用 `__slots__` 要注意， `__slots__` 定义的属性仅对当前类实例起作用，对继承的子类是不 起作用的。

##### 2. 使用 `@property`

再给示例绑定属性的时候，如果我们直接把属性暴露出去，虽然写起来很简单，但是，没办法检查参数，导致可以把成绩随意修改。

这显然不合逻辑。为了限制 score 的范围，可以通过一个 `set_score()` 方法来设置成绩，再通过一个 `get_score()` 来获取成绩，这样，在 `set_score()` 方法里，就可以检查参数：

```python
class Student(object):
    def get_score(self):
        return self._score
    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

```

但是，上面的调用方法又略显复杂，没有直接用属性这么直接简单。

`@property` 用于把方法伪装成属性，写法更自然。并且可以结合 `.setter` 和 `.deleter` 来控制属性的修改和删除。

```python
class Student(object):
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score必须是一个整数!')
        if value < 0 or value > 100:
            raise ValueError('score必须在0~100!')
        self._score = value
    @score.deleter
    def score(self):
        print("删除score属性")
        del self._score
```

调用的方式如下：

```python
s = Student()
s.score = 99 # setter
print(s.score) # getter
del s.score # deleter
```

还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性：

```python
class Student:
    @property
    def birth(self):
        return self._birth
    @birth.setter
    def birth(self,value):
        self._birth = value
    @property
    def age(self):
        return 2025 - self.birth
```

上面的birth是可读写属性，而age就是一个只读属性，因为age可以根据birth和当前时间计算出来。

注意：属性方法名和实例变量重名，会造成递归调用，导致栈溢出报错！

##### 3. 多重继承

通过多重继承，一个子类就可以同时获得多个父类的所有功能。

在设计类的继承关系时，通常，主线都是单一继承下来的，例如，Ostrich继承自Bird。但是，如果需要“混入”额外的功能，通过多重继承就可以实现，比如，让Ostrich除了继承自Bird外，再同时继承Runnable。这种设计通常称之为MixIn。

```python
class Animal(object):
    pass
class Mammal(Animal):
    pass
class Bird(Animal):
    pass
class Runnable(object):
    def run(self):
        print('Running...')
class Flyable(object):
    def fly(self):
        print('Flying...')
class Dog(Mammal,Runnable):
    pass
class Bat(Mammal,Flyable):
    pass
class Parrot(Bird,Flyable):
    pass
class Ostrich(Bird,Runnable):
    pass
```

为了更好地看出继承关系，我们把Runnable和Flyable改为RunnableMixIn和FlyableMixIn。类似的，你还可以定义出肉食动物CarnivorousMixIn和植食动物HerbivoresMixIn，让某个动物同时拥有好几个MixIn：

```python
class Dog(Mammal, RunnableMixIn, CarnivorousMixIn):
    pass
```

MixIn的目的就是给一个类增加多个功能，这样，在设计类的时候，我们优先考虑通过多重继承 来组合多个MixIn的功能，而不是设计多层次的复杂的继承关系。

Python自带的很多库也使用了MixIn。举个例子，Python自带了TCPServer和UDPServer这 两类网络服务，而要同时服务多个用户就必须使用多进程或多线程模型，这两种模型由ForkingMixIn和ThreadingMixIn提供。通过组合，我们就可以创造出合适的服务来。

```python
# 定义一个多进程模式的TCP服务
class MyTCPServer(TCPServer, ForkingMixIn):
    pass
# 定义一个多线程模式的UDP服务
class MyUDPServer(UDPServer, ThreadingMixIn):
    pass
```

这样一来，我们不需要复杂而庞大的继承链，只要选择组合不同的类的功能，就可以快速构造出所需的子类。

##### 4. 定制类

看到类似 `__slots__` 这种形如 `__xxx__` 的变量或者函数名就要注意，这些在Python中是有特殊用途的。 `__slots__` 我们已经知道怎么用了， `__len__()` 方法我们也知道是为了能让class作用于 `len()` 函数。 除此之外，Python的class中还有许多这样有特殊用途的函数，可以帮助我们定制类。

- `__str__` 和 `__repr__`

直接打印一个示例，会打印出形如 `<__main__.Student object at 0x109afb190>` 的信息。

`__str__` 方法，作用是定义“对象的非正式字符串表示”，主要用于 **用户友好的输出** ，其触发时机为 `print(obj)` 和 `str(obj)` 。

 ```python
 class Student(object):
     def __init__(self, name):
         self.name = name
     def __str__(self):
         return f'Student object (name: {self.name})'
     
 s = Student('Michael')    
 print(s) # Student object (name: Michael)
 print(str(s)) # Student object (name: Michael)
 ```

`__repr__` 方法，作用是定义“对象的官方字符串表示”，主要用于 **调试和开发** ，其触发时机为：（1）在交互式解释器里直接输入实例对象名；（2）调用 `repr(obj)` 时；（3）没有实现 `__str__` 时，`str(obj)` 会回退到 `__repr__`。

通常 `__str__()` 和 `__repr__()` 代码都是一样的， 所以，有个偷懒的写法：

```python
class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f'Student object (name={self.name})' 
    __repr__ = __str
```

- `__iter__` 和 `__next__`

如果一个类想被用于 `for ... in` 循环，类似list或tuple那样，就必须实现一个 `__iter__()` 方法，该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的 `__next__()` 方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。

```python
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回

nums = Fib()
for n in nums:
    print(n)
```

- `__getitem__`

Fib实例对象虽然能作用于for循环，但并不能按照下标取出元素。要表现得像list那样 **按照下标取出元素** ，需要实现 `__getitem__()` 方法：

```python
class Fib(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a
nums = Fib()
print(nums[5])
```

如果要使Fib实例对象可以 **切片** ，则可以做如下改进：

```python
class Fib(object):
    def __getitem__(self, n):  # 对传入的 n 进行判断
        if isinstance(n, int):  # n 是整数，下标访问
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a

        if isinstance(n, slice):  # n 是切片，形如 f[2:6]
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

nums = Fib()
print(nums[：5])
```

我们可以发现，我们还没有对step参数作处理，也没有对负数作处理，所以，要正确实现一个 `__getitem__()` 还是有很多工作要做的。此外，如果把对象看成dict ， `__getitem__()` 的参数也可能是一个可以作key的object，例如str。 与之对应的是 `__setitem__()` 方法，把对象视作list或dict来对集合赋值。最后，还有一个 `__delitem__()` 方法，用于删除某个元素。 总之，通过上面的方法，我们自己定义的类表现得和Python自带的list、tuple、dict没什么区别，这完全归功于动态语言的“鸭子类型”，不需要强制继承某个接口。

- `__gerattr__`

正常情况下，当我们调用类的方法或属性时，如果不存在，就会报错。要避免这个错误，除了可以加上一个score属性外，Python还有另一个机制，那就是写一个 `__getattr__()` 方法，动态返回一个属性。

```python
class Student(object):
    def __init__(self):
        self.name = 'Michael'
    def __getattr__(self, attr):
        if attr=='score':
            return 99
```

当调用不存在的属性时，比如score，Python解释器会试图调用 `__getattr__(self, 'score')` 来尝试获得属性，这样，我们就有机会返回score的值。

```python
>>> s = Student()
>>> s.name
'Michael'
>>> s.score
99
```

与此同时，返回函数也是完全可以的：

```python
class Student(object):
    def __getattr__(self, attr):
        if attr=='age':
            return lambda: 25
    
s = Student()
s.age()  # 25
```

只有在没有找到属性的情况下，才调用 `__getattr__` ，已有的属性，比如name，不会在 `__getattr__` 中查找。此外，注意到任意调用如 `s.abc` 都会返回 `None` ，这是因为我们定义的 `__getattr__` 默认返回就是 `None` 。要让class只响应特定的几个属性，我们就要按照约定，抛出 `AttributeError` 的错误：

```	python
class Student(object):
    def __getattr__(self, attr):
        if attr=='age':
            return lambda: 25
        raise AttributeError(f"\'Student\' object has no attribute \'{attr}\'")
```

##### 5. 使用枚举类

为枚举类型定义一个class类型，然后，每个常量都是class的一个唯一实例。可以直接使用 `Month.Jan` 来引用一个常量，或者枚举它的所有成员：

```python
>>> from enum import Enum
>>> Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
>>> for name, member in Month.__members__.items():
...     print(name, '=>', member, ',', member.value)
...
Jan => Month.Jan , 1
Feb => Month.Feb , 2
Mar => Month.Mar , 3
Apr => Month.Apr , 4
May => Month.May , 5
Jun => Month.Jun , 6
Jul => Month.Jul , 7
Aug => Month.Aug , 8
Sep => Month.Sep , 9
Oct => Month.Oct , 10
Nov => Month.Nov , 11
Dec => Month.Dec , 12
```

其中的 `value` 属性是自动赋给成员的int常量，默认从1开始计数。

如果需要更精确地控制枚举类型，可以从 `Enum` 派生出自定义类，其中的 `@unique` 装饰器可以帮助我们检查保证没有重复值：

```python
from enum import Enum, unique

@unique
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
```

访问这些枚举类型可以有若干种方法，既可以用成员名称引用枚举常量，又可以直接根据value的值获得枚举常量：

```python
>>> day1 = Weekday.Mon
>>> print(day1)
Weekday.Mon
>>> print(Weekday.Tue)
Weekday.Tue
>>> print(Weekday['Tue'])
Weekday.Tue
>>> print(Weekday.Tue.value)
2
>>> print(day1 == Weekday.Mon)
True
>>> print(day1 == Weekday.Tue)
False
>>> print(Weekday(1))
Weekday.Mon
>>> print(day1 == Weekday(1))
True
>>> Weekday(7)
Traceback (most recent call last):
  ...
ValueError: 7 is not a valid Weekday
```

`Enum` 可以把一组相关常量定义在一个class中，且class不可变，而且成员可以直接比较。

##### 6. 使用元类

在Python中，`type()` 函数的行为取决于传入参数的类型：

- 当传入一个类名时，`type()` 会返回该类的元类（通常是 `<class 'type'>` ）。

```python
class MyClass: 
    pass
print(type(MyClass))  # 输出 <class 'type'>
```

- 当传入一个实例名时，`type()` 会返回该实例所属的类（即实例的直接类型）。

```python
obj = MyClass()
print(type(obj))  # 输出 <class '__main__.MyClass'>
```

这两种行为体现了Python的"一切皆对象"设计理念——类本身也是对象（元类的实例），而实例则是类的对象。通过 `type()` 的返回值可以清晰区分元类、类和实例这三层关系。

由此可见，`type()` 函数既可以返回一个对象的类型，又可以创建出新的类型，比如，我们可以通过 `type()` 函数动态地创建出 `Hello` 类，而无需通过 `class Hello(object)...` 的定义：

```python
>>> def fn(self, name='world'): # 先定义函数
... 	print(f'Hello, {name}.')
...
>>> Hello = type('Hello', (object,), dict(hello=fn)) # 创建Hello class
>>> h = Hello()
>>> h.hello()
Hello, world.
>>> print(type(Hello))
<class 'type'>
>>> print(type(h))
<class '__main__.Hello'>
```

要创建一个class对象， `type()` 函数依次传入3个参数（类名，基类元组，属性字典）：

1. class的名称；
2. 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
3. class的方法名称与函数绑定，这里我们把函数 `fn` 绑定到方法名 `hello` 上。

通过 `type()` 函数创建的类和直接写class是完全一样的，因为Python解释器遇到class定义时， 仅仅是扫描一下class定义的语法，然后调用 `type()` 函数创建出class。 

mataclass部分的内容先省略。

### 错误、调试和测试

##### 1. 错误处理

Python内置的 `try...except...` 用来捕获错误十分方便。出错时，会分析错误信息并定位错误发生的代码位置才是最关键的。 

- `else`：当 `try` 语句块里没有异常时执行

- `finally`：无论是否出错都会执行（常用于清理资源）

```python
try:
    print('try...')
    r = 10 / int('2')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('no error!')
finally:
    print('finally...')
```

程序也可以主动抛出（raise）错误，让调用者来处理相应的错误。但是，应该在文档中写清楚可能会抛出哪些错误，以及错误产生的原因：

```python
def divide(a, b):
    if b == 0:
        raise ValueError("b 不能为 0")
    return a / b

print(divide(10, 2))
print(divide(10, 0))  # 会触发 ValueError
```

自定义异常类，继承内置 `Exception`，可以定义自己的业务逻辑错误类型：

```python
class MyError(Exception):
    pass

try:
    raise MyError("自定义错误")
except MyError as e:
    print("捕获到自定义异常：", e)
```

Python内置的 `logging` 模块可以把异常信息写入日志，便于排查：

```	python
import logging

logging.basicConfig(level=logging.ERROR)

try:
    1 / 0
except ZeroDivisionError as e:
    logging.error("发生错误", exc_info=True)
```

##### 2. 调试

- print() 打印变量值
- assert 断言

```python
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n
def main():
    foo('0')
```

如果断言失败， `assert` 语句本身就会抛出 `AssertionError` ：

```python
$ python err.py
Traceback (most recent call last):
  ...
AssertionError: n is zero!
```

启动Python解释器时可以用 `-O` 参数来关闭 `assert` ，关闭后，你可以把所有的 `assert` 语句当成 `pass` 来看：

```python
$ python -O err.py
Traceback (most recent call last):
  ...
ZeroDivisionError: division by zero
```

- logging

把 `print()` 替换为 `logging` 是第3种方式，和 `assert` 比，`logging` 不会抛出错误，而且可以输出到文件：

```python
import logging
logging.basicConfig(level=logging.INFO)

s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)
```

运行后输出了：

```python
$ python err.py
INFO:root:n = 0
Traceback (most recent call last):
  File "err.py", line 8, in <module>
    print(10 / n)
ZeroDivisionError: division by zero
```

`logging` 允许你指定记录信息的级别，有 `debug` ， `info` ， `warning` ， `error` 等几个级别，当我们指定 `level=INFO` 时， `logging.debug` 就不起作用了。同理，指定 `level=WARNING` 后， `debug` 和 `info` 就不起作用了。这样一来，你可以放心地输出不同级别的信息，也不用删除，最后统一控制输出哪个级别的信息。 

此外，`logging` 还可以通过简单的配置，一条语句可以同时输出到不同的地方，比如console和文件。

- IDE

如果要比较爽地设置断点、单步执行，就需要一个支持调试功能的IDE。目前比较好的Python IDE有：

Visual Studio Code：https://code.visualstudio.com/，需要安装Python插件。 

PyCharm：http://www.jetbrains.com/pycharm/ 

另外，Eclipse加上pydev插件也可以调试Python程序。

【小结】

写程序最痛苦的事情莫过于调试，程序往往会以你意想不到的流程来运行，你期待执行的语句其实根本没有执行，这时候，就需要调试了。 虽然用IDE调试起来比较方便，但是最后你会发现，logging才是终极武器。

##### 3. 单元测试

单元测试是用来对一个模块、一个函数或者一个类来进行正确性检验的测试工作。 

比如对函数 abs() ，我们可以编写出以下几个测试用例： 

1. 输入正数，比如 `1` 、 `1.2` 、 `0.99` ，期待返回值与输入相同； 
2. 输入负数，比如 `-1` 、 `-1.2` 、 `-0.99` ，期待返回值与输入相反；
3. 输入 `0` ，期待返回 `0` ；
4. 输入非数值类型，比如 `None` 、 `[]` 、 `{}` ，期待抛出 `TypeError` 。 把上面的测试用例放到一个测试模块里，就是一个完整的单元测试。

先来写个待测试类， `mydict.py` :

```python
class Dict(dict):
    def __init___(self,**kw):
        super().__init__(**kw)

    def __grtattr__(self,key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(f"'Dict' object has no attribute '{key}'")

    def __setattr__(self,key,value):
        self[key] = value
```

然后写测试类， `mydict_test.py` :

```python
import unittest

from mydict import Dict

class TestDict(unittest.TestCase):
    
    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty

if __name__ == '__main__':
    unittest.main()
```

一旦编写好单元测试，我们就可以运行单元测试。最简单的运行方式是在 `mydict_test.py` 的最后加上两行代码，这样就可以把它当做正常的python脚本运行：：

```python
if __name__ == '__main__':
    unittest.main()
```

另一种方法是在命令行通过参数 `-m unittest` 直接运行单元测试，这是推荐的做法，因为这样可以一次批量运行很多单元测试，并且，有很多工具可以自动来运行 这些单元测试：

```python
$ python -m unittest mydict_test
.....
----------------------------------------------------------------------
Ran 5 tests in 0.000s
OK
```

在开发阶段，很多时候，我们希望反复执行某一个测试方法，例如 `test_attr()` ，而不是每次都运行所有的测试方法，可以通过指定 `module.class.method` 来运行单个测试方法：

```python
$ python -m unittest mydict_test.TestDict.test_attr
.
----------------------------------------------------------------------
Ran 1 test in 0.000s
OK
```

其中， `module` 是文件名 `mydict_test` （不含 .py ）， `class` 是测试类 `TestDict` ， `method` 是指定的测试方法名 `test_attr` 。

也可以在单元测试中编写两个特殊的 `setUp()` 和 `tearDown()` 方法。这两个方法会分别在每调用一个测试方法的前后分别被执行。

`setUp()` 和 `tearDown()` 方法有什么用呢？设想你的测试需要启动一个数据库，这时，就可以 在 `setUp()` 方法中连接数据库，在 `tearDown()` 方法中关闭数据库，这样，不必在每个测试方法中重复相同的代码：

```python
class TestDict(unittest.TestCase):
    def setUp(self):
        print('setUp...')
    def tearDown(self):
        print('tearDown...')
```

【小结】

- 单元测试可以有效地测试某个程序模块的行为，是未来重构代码的信心保证。 
- 单元测试的测试用例要覆盖常用的输入组合、边界条件和异常。
- 单元测试代码要非常简单，如果测试代码太复杂，那么测试代码本身就可能有bug。
- 单元测试通过了并不意味着程序就没有bug了，但是不通过程序肯定有bug。

##### 4. 文档测试

当我们编写注释时，如果写上这样的注释，无疑明确地告诉函数的调用者该函数的期望输入和输出：

```python
def abs(n):
 '''
 Function to get absolute value of number.

 >>> abs(1)
 1
 >>> abs(-1)
 1
 >>> abs(0)
 0
 '''
 return n if n >= 0 else (-n)
```

Python内置的“文档测试”（doctest）模块可以直接提取注释中的代码并执行测试。

doctest严格按照Python交互式命令行的输入和输出来判断测试结果是否正确。只有测试异常的时候，可以用 `...` 表`示中间一大段烦人的输出。

当模块正常导入时，doctest不会被执行。只有在命令行直接运行时，才执 行doctest。所以，不必担心doctest会在非测试环境下执行。

```python
if __name__ == '__main__':
	import doctest
	doctest.testmod()
```

运行结果为什么输出也没有，这说明我们编写的doctest运行都是正确的。

【小结】

doctest不但可以用来测试，还可以直接作为示例代码。通过某些文档生成工具，就可以自动把包含doctest的注释提取出来。用户看文档的时候，同时也看到了doctest。

### IO编程

##### 1. 文件读写

首先是读文件，可以使用Python内置的 `open()` 函数，传入文件名和标示符：

```python
>>> f = open('/Users/michael/test.txt', 'r')
```

其中， `'r'` 表示只读，这样就成功地打开了一个文件。

若文件不存在， `open()` 函数就会抛出一个 `IOError` 的错误：

```python
>>> f = open('/Users/michael/notfound.txt', 'r')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileNotFoundError: [Errno 2] No such file or directory:
'/Users/michael/notfound.txt'
```

如果文件打开成功，接下来，调用 `read()` 方法可以一次读取文件的全部内容，Python把内容读到内存，用一个 `str` 对象表示：

```python
>>> f.read()
'Hello, world!'
```

最后一步是调用 `close()` 方法关闭文件。文件使用完毕后必须关闭，因为文件对象会占用操作系统的资源，并且操作系统同一时间能打开的文件数量也是有限的： 

```python
>>> f.close()
```

由于文件读写时都有可能产生 `IOError` ，一旦出错，后面的 `f.close()` 就不会调用。所以，为了保证无论是否出错都能正确地关闭文件，我们可以使用 `try ... finally` 来实现：

```python
try:
	f = open('/path/to/file', 'r')
 	print(f.read())
finally:
	if f:
		f.close()
```

但是每次都这么写实在太繁琐，所以，Python引入了 `with` 语句（语法糖）来自动帮我们调用 `close()` 方法：

```python
with open('/path/to/file', 'r') as f: 
    print(f.read())
```

读取方式也有多种，可以根据需要决定怎么调用：

- 调用 `read()` 会一次性读取文件的全部内容
- 调用 `read(size)` 方法，每次最多读取size个字节的内容
- 调用 `readline()` 每次读取一行内容
- 调用 `readlines()` 一次读取所有内容并按行返回 `list` 

如果文件很小， `read()` 一次性读取最方便；如果不能确定文件大小，反复调用 `read(size)` 比较保险；如果是配置文件，调用 `readlines()` 最方便：

```python
for line in f.readlines():
	print(line.strip()) # 把末尾的'\n'删掉
```

值得一提的是，前面讲的默认都是读取 **文本文件** ，并且是UTF-8编码的文本文件。要读取 **二进制文件** ，比如图 片、视频等等，用 `'rb'` 模式打开文件即可：

```python
>>> f = open('/Users/michael/test.jpg', 'rb')
>>> f.read()
b'\xff\xd8\xff\xe1\x00\x18Exif\x00\x00...' # 十六进制表示的字节
```

要读取非UTF-8编码的文本文件，需要给 `open()` 函数传入 `encoding` 参数，例如，读取GBK编码的文件：

```python
>>> f = open('/Users/michael/gbk.txt', 'r', encoding='gbk')
>>> f.read()
'测试'
```

遇到有些编码不规范的文件，可能会遇到 `UnicodeDecodeError` ，因为在文本文件中可能夹杂了一些非法编码的字符。遇到这种情况，`open()` 函数还接收一个 `errors` 参数，表示如果遇到编码错误后如何处理。最简单的方式是直接忽略：

```python
>>> f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore')
```

再来说说写文件，其与读文件是一样的，唯一区别是调用 `open()` 函数时，传入标识符 `'w'` 或者 `'wb'` 表示写文本文件或写二进制文件：

```python
>>> f = open('/Users/michael/test.txt', 'w')
>>> f.write('Hello, world!')
>>> f.close()
```

你可以反复调用 `write()` 来写入文件，但是务必要调用 `f.close()` 来关闭文件。当我们写文件时，操作系统往往不会立刻把数据写入磁盘，而是放到内存缓存起来，空闲的时候再慢慢写入。只有调用 `close()` 方法时，操作系统才保证把没有写入的数据全部写入磁盘。忘记调用 `close()` 的后果是数据可能只写了一部分到磁盘，剩下的丢失了。所以，还是用 `with` 语句来得保险：

```python
with open('/Users/michael/test.txt', 'w') as f:
	f.write('Hello, world!')
```

此外，要写入特定编码的文本文件，请给 `open()` 函数传入 `encoding` 参数，将字符串自动转换成指定编码。以 `'w'` 模式写入文件时，如果文件已存在，会直接覆盖（相当于删掉后新写入一个文件）。如果我们希望追加到文件末尾，可以传入 `'a'` 以追加（append）模式写入。

##### 2. 操作文件和目录

操作文件和目录的函数一部分放在 `os` 模块中，一部分放在 `os.path` 模块中。查看、创建和删除目录可以这么调用：

```python
# 查看当前目录的绝对路径:
>>> os.path.abspath('.')
'/Users/michael'
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
>>> os.path.join('/Users/michael', 'testdir')
'/Users/michael/testdir'
# 然后创建一个目录:
>>> os.mkdir('/Users/michael/testdir')
# 删掉一个目录:
>>> os.rmdir('/Users/michael/testdir')
```

注意，把两个路径合成一个时，不要直接拼字符串，而要通过 `os.path.join()` 函数，这样可以正确处理不同操作系统的路径分隔符。

同样的道理，要拆分路径时，也不要直接去拆字符串，而要通过 `os.path.split()` 函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名：

```python
>>> os.path.split('/Users/michael/testdir/file.txt')
('/Users/michael/testdir', 'file.txt')
```

`os.path.splitext()` 可以直接让你得到文件扩展名，返回一个元组，这在很多时候非常方便：

```python
>>> os.path.splitext('/path/to/file.txt')
('/path/to/file', '.txt')
```

这些合并、拆分路径的函数并不要求目录和文件要真实存在，它们只对字符串进行操作。

利用Python的特性来过滤文件。比如我们要列出当前目录下的所有目录，只需要一行代码：

```python
>>> [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']
['xxx.py', ...]
```

##### 3. 序列化

我们把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，在其他语言中也被称之为serialization，marshalling，flattening等等，都是一个意思。 序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。 

反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。

Python提供了 `pickle` 模块来实现序列化。 

- `pickle.dumps()` 方法把任意obj序列化成一个bytes，然后，就可以把这个bytes写入文件。

```python
import pickle

data = {"name": "Alice", "age": 25, "scores": [95, 88, 76]}
serialized = pickle.dumps(d)
print(serialized)
```

- 或者用另一个方法 `pickle.dump()` 直接把对象序列化后写入一个file-like Object：

```python
with open("data.txt", "wb") as f:
	pickle.dump(data, f)
```

- 反序列化，可以使用`pickle.load()` 方法从文件中读取对象：

```python
import pickle

with open("data.pkl", "rb") as f:
    loaded_data = pickle.load(f)
print(loaded_data)
```

- 也可以通过`pickle.loads(bytes_obj)` 方法从字节串恢复对象：

```python
restored = pickle.loads(serialized)
print(restored)
```

