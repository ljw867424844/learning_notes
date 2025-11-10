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

其中，标示符 `'r'` 表示只读，这样就成功地打开了一个文件。

若文件不存在， `open()` 函数就会抛出一个 `IOError` 的错误：

```python
>>> f = open('/Users/michael/notfound.txt', 'r')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileNotFoundError: [Errno 2] No such file or directory:'/Users/michael/notfound.txt'
```

如果文件打开成功，接下来我们可以调用 `read()` 方法，一次读取文件的全部内容，Python把内容读到内存，用一个 `str` 对象表示：

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

注意：每次调用 `f.read(size)` 都会从上次读取的位置继续往后读。操作文件指针位置的方法有：

- `f.tell()`：返回当前读取位置。

- `f.seek(offset)`：移动文件指针。

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

以 `'w'` 模式写入文件时，如果文件已存在，会直接覆盖。如果我们希望追加到文件末尾，可以传入 `'a'` 以追加模式写入。

##### 2. 操作文件和目录

操作文件和目录的函数一部分放在 `os` 模块中，一部分放在 `os.path` 模块中。**查看、创建和删除目录**可以这么调用：

```python
# 1.查看当前目录的绝对路径:
>>> os.path.abspath('.')
'/Users/michael'
# 2.把新目录的完整路径表示出来:
>>> os.path.join('/Users/michael', 'testdir')
'/Users/michael/testdir'
# 3.然后创建一个目录:
>>> os.mkdir('/Users/michael/testdir')
# 4.删掉一个目录:
>>> os.rmdir('/Users/michael/testdir')
```

注意，把两个路径合成一个时，**不要直接拼字符串**，而要通过 `os.path.join()` 函数，这样可以正确处理不同操作系统的路径分隔符。

同样的道理，要拆分路径时，也不要直接去拆字符串，而要通过 `os.path.split()` 函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名：

```python
>>> os.path.split('/Users/michael/testdir/file.txt')
('/Users/michael/testdir', 'file.txt')
```

`os.path.splitext()` 可以直接让你得到**文件扩展名**，返回一个**元组**，这在很多时候非常方便：

```python
>>> os.path.splitext('/path/to/file.txt')
('/path/to/file', '.txt')
```

注意，这些合并、拆分路径的函数并不要求目录和文件要真实存在，它们只对字符串进行操作。

利用Python的特性来过滤文件。比如我们要列出当前目录下的所有py文件，只需要一行代码：

```python
>>> [x for x in os.listdir('.') if os.path.splitext(x)[1] == '.py']
['xxx.py', ...]
```

##### 3. 序列化

我们把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，在其他语言中也被称之为serialization，marshalling，flattening等等，都是一个意思。 序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。 反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。

Python提供了 `pickle` 模块来实现序列化： 

- `pickle.dumps()` 方法把任意obj序列化成一个bytes。

```python
import pickle

data = {"name": "Alice", "age": 25, "scores": [95, 88, 76]}
serialized = pickle.dumps(data)
print(serialized)
```

- 或者用另一个方法 `pickle.dump()` 直接把对象序列化后写入文件：

```python
with open("data.pkl", "wb") as f:
	pickle.dump(data, f)
```

- 反序列化，可以使用`pickle.load()` 方法从文件中读取对象：

```python
import pickle

with open("data.pkl", "rb") as f:
    loaded_data = pickle.load(f)
print(loaded_data)
```

- 也可以通过`pickle.loads(bytes_obj)` 方法从字节串恢复到对象：

```python
restored = pickle.loads(serialized)
print(restored)
```

Pickle只能用于Python，并且可能不同版本的Python彼此都不兼容。如果我们要在不同的编程语言之间传递对象，就必须把对象序列化为标准格式，比如XML，但更好的方法是序列化为JSON，因为JSON表示出来就是一个字符串，可以被所有语言读取，也可以方便地存储到磁盘或者通过网络传输。JSON不仅是标准格式，并且比XML更快，而且可以直接在Web页面中读取，非常方便。

Python内置的 `json` 模块提供了非常完善的从 **对象** 到 **JSON** 的转换：

```python
>>> import json
>>> data = {'name':'Bob', 'age':20, 'score':88}
>>> json.dumps(data)
'{"age": 20, "score": 88, "name": "Bob"}'
```

- json模块的 ` dumps()` 方法返回一个 `str` ，内容就是标准的JSON。

值得一提的是，对中文进行JSON序列化时， `json.dumps()` 提供了一个 `ensure_ascii` 参数：

```python
import json

obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=True)
print(s)
```

`json.dumps()` 默认假设所有字符串都要用 **ASCII 编码**。 因此，所有非 ASCII 字符（例如中文、表情符号等）都会被 **转义** 成 `\uXXXX` 的形式。如果你想让JSON中显示真正的中文，而不是Unicode转义，就可以设置：

```python
json.dumps(obj, ensure_ascii=False)
```

- json模块的 `dump()` 方法可以直接把 JSON写入一个 `file-like Object` 。

```python
>>> import json
>>> data = {'name':'Bob', 'age':20, 'score':88}
>>> with open('data.json','w') as f:
... ... json.dump(data,f)
... 
```

反过来，要把JSON反序列化为Python对象，用 `loads()` 或者对应的 `load()` 方法，前者把JSON的字符串反序列化，后者从 `file-like Object` 中读取字符串并反序列化：

```python
>>> json_str = '{"age": 20, "score": 88, "name": "Bob"}'
>>> json.loads(json_str)
{'age': 20, 'score': 88, 'name': 'Bob'}
>>> with open("data.json", "r") as f:
... ... json.load(f)
... 
{'age': 20, 'score': 88, 'name': 'Bob'}
```

Python的 `dict` 对象可以直接序列化为JSON格式，不过，很多时候，我们更喜欢用 `class` 表示对象，比如定义 `Student` 类，然后序列化：

```python
import json

class Student(object):
	def __init__(self, name, age, score):
		self.name = name
 		self.age = age
 		self.score = score

stu = Student('Bob', 20, 88)

# 方法一：手动转为 dict，最简单、最常用的方法。
stu_dict = {"name": stu.name, "age": stu.age, "score": stu.score}
json_str = json.dumps(stu_dict)
print(json_str)

# 方法二：使用 __dict__ 自动转成字典，Python对象内部都有一个 __dict__ 属性，用于存储实例变量。
json_str = json.dumps(stu.__dict__)
print(json_str)

# 方法三：使用 default 参数
def student2dict(s):
	return {'name': s.name,'age': s.age,'score': s.score}
json_str = json.dumps(stu, default=student2dict)
print(json_str)
```

同样的道理，如果我们要把JSON反序列化为一个 `Student` 对象实例， `loads()` 方法首先转换出一个 `dict` 对象，然后，我们传入的 `object_hook` 函数负责把 `dict` 转换为 `Student` 实例：

```python
>>> def dict2student(d):
... ... return Student(d['name'], d['age'], d['score'])
...
>>> json_str = '{"age": 20, "score": 88, "name": "Bob"}'
>>> print(json.loads(json_str, object_hook=dict2student))
<__main__.Student object at 0x10cd3c190>
```

【小结】

Python语言特定的序列化模块是 `pickle` ，但如果要把序列化搞得更通用、更符合Web标准， 就可以使用 `json` 模块。 `json` 模块的 `dumps()` 和 `loads()` 函数是定义得非常好的接口的典范。当我们使用时，只需要传入一个必须的参数。但是，当默认的序列化或反序列机制不满足我们的要求时，我们又可以传入更多的参数来定制序列化或反序列化的规则，既做到了接口简单易用，又做到了充分的扩展性和灵活性。

### 进程和线程

##### 1. 多进程

Unix/Linux操作系统提供了一个 `fork()` 系统调用，它非常特殊。普通的函数调用，调用一次， 返回一次，但是 `fork()` 调用一次，返回两次，因为操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），然后，分别在父进程和子进程内返回。 子进程永远返回 0 ，而父进程返回子进程的ID。这样做的理由是，一个父进程可以fork出很多子进程，所以，父进程要记下每个子进程的ID，而子进程只需要调用 `getppid()` 就可以拿到父进程的ID。

有了 `fork` 调用，一个进程在接到新任务时就可以复制出一个子进程来处理新任务，常见的Apache服务器就是由父进程监听端口，每当有新的http请求时，就 `fork` 出子进程来处理新的http请求。

Windows系统没有fork调用，但是，Python提供了 **multiprocessing模块** 用于多进程并发编程，一个 `Process` 类来代表一个进程对象，下面的例子演示了启动 一个子进程并等待其结束：

```python
from multiprocessing import Process
import os

# 子进程要执行的代码
def run_proc(name):
	print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
 	p = Process(target=run_proc, args=('test',))
 	print('Child process will start.')
 	p.start()
 	p.join()
 	print('Child process end.')
```

运行结果如下：

```python
Parent process 936.
Child process will start.
Run child process test (937)...
Child process end.
```

- 创建子进程时，只需要传入一个执行函数和函数的参数，创建一个 `Process` 实例，用 `start()` 方法启动。
-  `join()` 方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。

如果要启动大量的子进程，可以用 **进程池** 的方式批量创建子进程：

```python
from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i+1,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')
```

运行结果如下：

```python
Parent process 3.
Run task 3 (5)...
Task 3 runs 0.46 seconds.
Run task 1 (4)...
Task 1 runs 0.49 seconds.
Run task 2 (6)...
Task 2 runs 0.20 seconds.
Run task 5 (6)...
Task 5 runs 2.27 seconds.
Run task 4 (7)...
Task 4 runs 0.30 seconds.
Waiting for all subprocesses done...
All subprocesses done.
```

对 `Pool` 对象调用 `join()` 方法会等待所有子进程执行完毕，调用 `join()` 之前必须先调用 `close()` ，调用 `close()` 之后就不能继续添加新的 `Process` 了。 

请注意输出的结果，task `1` ， `2` ， `3` ， `4` 是立刻执行的，而task `5` 要等待前面某个task完成后才执行，这是因为 `Pool` 的默认大小在我的电脑上是4，因此，最多同时执行4个进程。这是 `Pool` 有意设计的限制，并不是操作系统的限制。如果改成：`p = Pool(5)` ，就可以同时跑5个进程。

由于 `Pool` 的默认大小是CPU的核数，如果你拥有8核CPU，你要提交至少9个子进程才能看到上面的等待效果。

Process 之间肯定是需要通信的，操作系统提供了很多机制来实现 **进程间的通信（IPC）** 。Python的 `multiprocessing` 模块包装了底层的机制，提供了 `Queue` 、 `Pipes` 等多种方式来交换数据。 我们以 `Queue` 为例，在父进程中创建两个子进程，一个往 `Queue` 里写数据，一个从 `Queue` 里读数据：

```python
from multiprocessing import Process, Queue
import os, time, random

# 写数据进程执行的代码:
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

# 读数据进程执行的代码:
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)

if __name__ == '__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()
```

运行结果为：

```python
Process to write: 12756
Put A to queue...
Process to read: 4564
Get A from queue.
Put B to queue...
Get B from queue.
Put C to queue...
Get C from queue.
```

【小结】

在Unix/Linux下，可以使用 `fork()` 调用实现多进程。 要实现跨平台的多进程，可以使用 `multiprocessing` 模块。 进程间通信是通过 `Queue` 、 `Pipes` 等实现的。

##### 2. 多线程

我们前面提到了进程是由若干线程组成的，一个进程至少有一个线程。 由于线程是操作系统直接支持的执行单元，因此，高级语言通常都内置多线程的支持，Python也不例外，并且，Python的线程是真正的Posix Thread，而不是模拟出来的线程。 

Python的标准库提供了两个模块： `_thread` 和 `threading` ， `_thread` 是低级模块， `threading` 是高级模块，对 `_thread` 进行了封装。绝大多数情况下，我们只需要使用 `threading` 这个高级模块。

启动一个线程就是把一个函数传入并创建 `Thread` 实例，然后调用 `start()` 开始执行：

```python
import time, threading

# 新线程执行的代码:
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)
```

执行结果如下：

```python
thread MainThread is running...
thread LoopThread is running...
thread LoopThread >>> 1
thread LoopThread >>> 2
thread LoopThread >>> 3
thread LoopThread >>> 4
thread LoopThread >>> 5
thread LoopThread ended.
thread MainThread ended.
```

由于任何进程默认就会启动一个线程，我们把该线程称为 **主线程** ，主线程又可以启动新的线程， Python的 `threading` 模块有个 `current_thread()` 函数，它永远返回当前线程的实例。主线程实例的名字叫 `MainThread` ，子线程的名字在创建时指定，我们用 `LoopThread` 命名子线程。 名字仅仅在打印时用来显示，完全没有其他意义，如果不起名字Python就自动给线程命名为 `Thread-1` ， `Thread-2` , ……

多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在于每个进程中， 互不影响，而多线程中，所有变量都由所有线程共享，所以，任何一个变量都可以被任何一个线程修改，因此，线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了。

如果我们要确保数据计算正确，就要给线程上一把锁，当某个线程开始执行时，我们说，该线程因为获得了锁，因此其他线程不能同时执行，只能等待，直到锁被释放后，获得该锁以后才能改。由于锁只有一个，无论多少线程，同一时刻最多只有一个线程持有该锁，所以，不会造成修改的冲突。创建一个锁是通过 `threading.Lock()` 来实现的：

```python
balance = 0
lock = threading.Lock()
def run_thread(n):
    for i in range(100000):
        # 先要获取锁:
        lock.acquire()
        try:
            # 放心地改吧:
            change_it(n)
        finally:
            # 改完了一定要释放锁:
            lock.release()
```

当多个线程同时执行 `lock.acquire()` 时，只有一个线程能成功地获取锁，然后继续执行代码， 其他线程就继续等待直到获得锁为止。 获得锁的线程用完后一定要释放锁，否则那些苦苦等待锁的线程将永远等待下去，成为死线程。 所以我们用 `try...finally` 来确保锁一定会被释放。

锁的好处就是确保了某段关键代码只能由一个线程从头到尾完整地执行，坏处当然也很多，首先是阻止了多线程并发执行，包含锁的某段代码实际上只能以单线程模式执行，**效率就大大地下降了**。其次，由于可以存在多个锁，不同的线程持有不同的锁，并试图获取对方持有的锁时，**可能会造成死锁**，导致多个线程全部挂起，既不能执行，也无法结束，只能靠操作系统强制终止。

Python的线程虽然是真正的线程，但解释器执行代码时，有一个**GIL锁（Global Interpreter Lock）**，任何Python线程执行前，必须先获得GIL锁，然后，每执行100条字节码，解释器就自动释放GIL锁，让别的线程有机会执行。这个GIL全局锁实际上把所有线程的执行代码都给上了锁， 所以，多线程在Python中只能交替执行，即使100个线程跑在100核CPU上，也只能用到1个核。

GIL是Python解释器设计的历史遗留问题，通常我们用的解释器是官方实现的CPython，要真正利用多核，除非重写一个不带GIL的解释器。

所以，在Python中，可以使用多线程，但不要指望能有效利用多核。如果一定要通过多线程利用 多核，那只能通过C扩展来实现，不过这样就失去了Python简单易用的特点。 不过，也不用过于担心，Python虽然不能利用多线程实现多核任务，但可以通过多进程实现多核任务。多个Python进程有各自独立的GIL锁，互不影响。

【小结】

多线程编程，模型复杂，容易发生冲突，必须用锁加以隔离，同时，又要小心死锁的发生。 Python解释器由于设计时有GIL全局锁，导致了多线程无法利用多核。

##### 3. ThreadLocal

在多线程环境下，每个线程都有自己的数据。一个线程使用自己的局部变量比使用全局变量好， 因为局部变量只有线程自己能看见，不会影响其他线程，而全局变量的修改必须加锁。但是局部变量也有问题，就是在函数调用的时候，传递起来很麻烦。`ThreadLocal` 应运而生：

```python
import threading

# 创建全局ThreadLocal对象:
local_school = threading.local()

def process_student():
    # 获取当前线程关联的student:
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.student = name
    process_student()

t1 = threading.Thread(target= process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target= process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()
```

全局变量 `local_school` 就是一个 `ThreadLocal` 对象，每个 `Thread` 对它都可以读写 `student` 属性，但互不影响。你可以把 `local_school` 看成全局变量，但每个属性如 `local_school.student` 都是线程的局部变量，可以任意读写而互不干扰，也不用管理锁的问 题， `ThreadLocal` 内部会处理。

`ThreadLocal` 最常用的地方就是为每个线程绑定一个数据库连接，HTTP请求，用户身份信息等，这样一个线程的所有调用到的处理函数都可以非常方便地访问这些资源。

【小结】

一个 `ThreadLocal` 变量虽然是全局变量，但每个线程都只能读写自己线程的独立副本，互不干扰。 `ThreadLocal` 解决了参数在一个线程中各个函数之间互相传递的问题。

### 正则表达式

正则表达式是一种用来匹配字符串的强有力的武器。它的设计思想是用一种描述性的语言来给字 符串定义一个规则，凡是符合规则的字符串，我们就认为它“匹配”了，否则，该字符串就是不合法的。

在正则表达式中，如果直接给出字符，就是精确匹配。用 `\d` 可以匹配一个数字， `\w` 可以匹配一个字母或数字，所以：

- `'00\d'` 可以匹配 `'007'` ，但无法匹配 `'00A'` ；
- `'\d\d\d'` 可以匹配 `'010'` ； 
- `'\w\w\d'` 可以匹配 `'py3'` ；

`.` 可以匹配任意字符，所以：

- `'py.'` 可以匹配 `'pyc'` 、 `'pyo'` 、 `'py!'` 等等。

要匹配变长的字符，在正则表达式中，用 `*` 表示任意个字符（包括0个），用 `+` 表示至少一个字符，用 `?` 表示0个或1个字符，用 `{n}` 表示n个字符，用 `{n,m}` 表示n-m个字符。

来看一个复杂的例子： `\d{3}\s+\d{3,8}` 。

1. `\d{3}` 表示匹配3个数字，例如 `'010'` ；
2. `\s` 可以匹配一个空格（也包括Tab等空白符），所以 `\s+` 表示至少有一个空格，例如匹配 `' '` ， `'   '` 等；
3. `\d{3,8}` 表示3-8个数字，例如 `'1234567'` 。

综合起来，上面的正则表达式可以匹配以任意个空格隔开的带区号的电话号码。

如果要匹配 `'010-12345'` 这样的号码呢？由于 `'-'` 是特殊字符，在正则表达式中，要用 `'\'` 转义，所以，上面的正则是 `\d{3}\-\d{3,8}` 。

要做更精确地匹配，可以用 `[]` 表示范围，比如：

- `[0-9a-zA-Z\_]` 可以匹配一个数字、字母或者下划线； 
- `[0-9a-zA-Z\_]+` 可以匹配至少由一个数字、字母或者下划线组成的字符串，比 如 `'a100'` ， `'0_Z'` ， `'Py3000'` 等等；
-  `[a-zA-Z\_][0-9a-zA-Z\_]*` 可以匹配由字母或下划线开头，后接任意个由一个数字、字母或者下划线组成的字符串，也就是Python合法的变量； 
- `[a-zA-Z\_][0-9a-zA-Z\_]{0, 19}` 更精确地限制了变量的长度是1-20个字符（前面1个字符 + 后面最多19个字符）。

`A|B` 可以匹配A或B，所以 `(P|p)ython` 可以匹配 `'Python'` 或者 `'python'` 。 

`^` 表示行的开头， `^\d` 表示必须以数字开头。 

`$` 表示行的结束， `\d$` 表示必须以数字结束。 

你可能注意到了， `py` 也可以匹配 `'python'` ，但是加上 `^py$` 就变成了整行匹配，就只能匹配 `'py'` 了。

Python提供 `re` 模块，包含所有正则表达式的功能。由于Python的字符串本身也用 `\` 转义，所以要特别注意：

```python
s = 'ABC\\-001' # Python的字符串
# 对应的正则表达式字符串变成 'ABC\-001'
```

因此我们强烈建议使用Python的 `r` 前缀，就不用考虑转义的问题了：

```python
s = r'ABC\-001' # Python的字符串
# 对应的正则表达式字符串不变：'ABC\-001'
```

如何判断正则表达式是否匹配：

```python
>>> import re
>>> re.match(r'^\d{3}\-\d{3,8}$', '010-12345')
<_sre.SRE_Match object; span=(0, 9), match='010-12345'>
>>> re.match(r'^\d{3}\-\d{3,8}$', '010 12345')
>>>
```

`match()` 方法判断是否匹配，如果匹配成功，返回一个 `Match` 对象，否则返回 `None` 。常见的判断方法就是：

```python
test = '用户输入的字符串'
if re.match(r'正则表达式', test):
	print('ok')
else:
	print('failed')
```

正常的切分字符串无法识别连续的空格：

```python
>>> 'a b   c'.split(' ')
['a', 'b', '', '', 'c']
```

而使用正则表达式无论多少个空格都可以正常分割:

```python
>>> re.split(r'\s+', 'a b   c')
['a', 'b', 'c']
```

如果用户输入了一组标签，下次记得用正则表达式来把不规范的输入转化成正确的数组:

```python
>>> re.split(r'[\s\,\;]+', 'a,b;;c   d')
['a', 'b', 'c', 'd']
```

除了简单地判断是否匹配之外，正则表达式还有提取子串的强大功能。

- 普通分组 `( ... )` 在正则中有两个功能：

1. 把子表达式作为整体（控制优先级）
2. 捕获匹配内容，可以通过 `group()` 方法取出来。 注意到 `group(0)` 永远是与整个正则表达式相匹配的字符串，而 `group(1)` 、 `group(2)` 、...表示第1、2、...个子串

- 非捕获分组`(?: ... )` 只保留分组功能，不会生成 `group(1)`、`group(2)` 这样的编号结果。

正则表达式可以直接识别合法的时间：

```python
>>> t = '19:05:30'
>>> m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
>>> m.groups()
('19', '05', '30')
```

但是有些时候，用正则表达式也无法做到完全验证， 比如识别日期：

```python
'^(0[1-9]|1[0-2]|[0-9])-(0[1-9]|1[0-9]|2[0-9]|3[0-1]|[0-9])$'
```

对于 `'2-30'` ， `'4-31'` 这样的非法日期，用正则还是识别不了，或者说写出来非常困难，这时就需要程序配合识别了。

值得一提的是，正则匹配默认是贪婪匹配，也就是匹配尽可能多的字符。举例如下，匹配出数字后面的 `0` ：

```python
>>> m = re.match(r'^(\d+)(0*)$', '102300').groups()
('102300', '')
```

由于 `\d+` 采用贪婪匹配，直接把后面的 `0` 全部匹配了，结果 `0*` 只能匹配空字符串了。 必须让 `\d+` 采用非贪婪匹配（也就是尽可能少匹配），才能把后面的 `0` 匹配出来，加个 `?` 就可以让 `\d+` 采用非贪婪匹配：

```python
>>> m = re.match(r'^(\d+?)(0*)$', '102300').groups()
('1023', '00')
```

当我们在Python中使用正则表达式时，re模块内部会干两件事情： 

1. 编译正则表达式，如果正则表达式的字符串本身不合法，会报错； 

2. 用编译后的正则表达式去匹配字符串。 

如果一个正则表达式要重复使用几千次，出于效率的考虑，我们可以预编译该正则表达式，接下来重复使用时就不需要编译这个步骤了，直接匹配：

```python
>>> import re
>>> re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
>>> re_telephone.match('010-12345').groups()
('010', '12345')
>>> re_telephone.match('010-8086').groups()
('010', '8086')
```

### 常用内建模块

##### 1. datetime

`datetime` 是Python处理日期和时间的标准库。

- 获取当前日期和时间：

```python
>>> from datetime import datetime
>>> now = datetime.now() # 获取当前datetime
>>> print(now)
2025-10-10 15:55:00.006017
>>> print(type(now))
<class 'datetime.datetime'>
```

其中，`datetime.now()` 返回当前日期和时间，其类型是 `datetime` 。

- 获取指定日期和时间：

```python
>>> from datetime import datetime
>>> dt = datetime(2025, 11, 11, 11, 11) # 用指定日期时间创建datetime
>>> print(dt)
2025-11-11 11:11:00
```

- datetime转换为timestamp（调用 `timestamp()` 方法）：

```python
from datetime import datetime

dt = datetime(2025, 10, 11, 10, 30, 0)
ts = dt.timestamp()
print(ts)
```

Python的timestamp是一个浮点数，整数位表示秒。 而某些编程语言（如Java和JavaScript）的timestamp使用整数表示毫秒数，这种情况下只需要把timestamp除以1000就得到Python的浮点表示方法。

- timestamp转换为datetime：

方法 1（转换为本地时间）：`datetime.fromtimestamp(ts)`

方法 2（转换为UTC时间）：`datetime.utcfromtimestamp(ts)`

本地时间是指当前操作系统设定的时区。例如北京时区是东8区，则本地时间：

```python
2025-10-10 16:00:00 
```

实际上就是UTC+8:00时区的时间：

```python
2025-10-10 16:00:00 UTC+8:00
```

而此刻的格林威治标准时间与北京时间差了8小时，也就是UTC+0:00时区的时间应该是：

```python
2025-10-10 08:00:00 UTC+0:00
```

- str转换为datetime：

很多时候，用户输入的日期和时间是字符串，要处理日期和时间，首先必须把str转换为datetime。转换方法是通过 `datetime.strptime()` 实现，需要一个日期和时间的格式化字符串：

```python
>>> from datetime import datetime
>>> cday = datetime.strptime('2025-12-12 12:12:12', '%Y-%m-%d %H:%M:%S')
>>> print(cday)
2025-12-12 12:12:12
```

转换后的datetime是没有时区信息的，字符串 `'%Y-%m-%d %H:%M:%S'` 规定了日期和时间部分的格式。

- datetime转换为str：

如果已经有了datetime对象，要把它格式化为字符串显示给用户，就需要转换为str，转换方法是通过 `strftime()` 实现的，同样需要一个日期和时间的格式化字符串：

```python
>>> from datetime import datetime
>>> dt = datetime(2025, 10, 11, 10, 30, 0)
>>> print(dt.strftime('%Y-%m-%d %H:%M:%S'))
2025-10-11 10:30:00
```

- datetime加减

 第一种：`datetime` 加减 `timedelta`

```python
>>> from datetime import datetime, timedelta
>>> dt = datetime(2025, 10, 11, 14, 30, 0)
>>> dt
datetime.datetime(2025, 10, 11, 14, 30)
>>> new_dt = dt + timedelta(days=5, hours=3)
>>> new_dt
datetime.datetime(2025, 10, 16, 17, 30)
>>> new_dt2 = dt - timedelta(days=2, minutes=15)
>>> new_dt2
datetime.datetime(2025, 10, 9, 14, 15)
```

第二种：`datetime` 之间的减法

```python
from datetime import datetime

dt1 = datetime(2025, 10, 11, 14, 30, 0)
dt2 = datetime(2025, 10, 8, 10, 0, 0)
delta = dt1 - dt2
print(delta)	# 3 days, 4:30:00
print(delta.days, "天")	# 3 天
print(delta.total_seconds(), "秒")	# 275400.0 秒
```

- 时区转换

第一步：给 `datetime` 添加时区

```python
from datetime import datetime, timezone, timedelta

# 当前 UTC 时间（无时区）
naive_utc = datetime.utcnow()

# 强制设置为 UTC+0（添加 tzinfo，不做时间偏移）
utc_dt = naive_utc.replace(tzinfo=timezone.utc)
print(utc_dt)
# 2025-10-11 09:57:52.083032+00:00
```

注意： `.replace(tzinfo=...)` 只是“标记”当前对象属于哪个时区，不改变时间数值。它不会做任何时间换算。

第二步：转换时区

```python
# 转换为北京时间（UTC+8）
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)
# 2025-10-11 17:58:24.301177+08:00

# 转换为东京时间（UTC+0）
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)
# 2025-10-11 18:58:40.350467+09:00
```

Python 会把 `utc_dt` 转成 `timestamp` ，再用目标时区重新表达出来。时间点相同，但显示的本地时间不同。

再试试把北京时间转成东京时间，时间与上面一致，因为两者都表示同一个 UTC 时刻：

```python
# 把北京时间转成东京时间
tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt2)
# 2025-10-11 18:59:07.875657+09:00
```

【小结】

`datetime` 表示的时间需要时区信息才能确定一个特定的时间，否则只能视为本地时间。

如果要存储 `datetime` ，最佳方法是将其转换为timestamp（调用 `timestamp()` 方法实现）再存储，因为timestamp的值与时区完全无关。

##### 2. collections

`collections` 模块提供了一些有用的集合类，可以根据需要选用。

- namedtuple

`namedtuple()` 函数用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。

```python
>>> from collections import namedtuple
>>> Point = namedtuple('Point', ['x', 'y'])
>>> p = Point(1, 2)
>>> p.x
1
>>> p.y
2
```

这样一来，我们用 `namedtuple` 可以很方便地定义一种数据类型，它具备tuple的不变性，又可以 **根据属性来引用**，使用十分方便。

- deque

使用 `list` 存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为 `list` 是线性存储，数据量大的时候，插入和删除效率很低。

而 `deque` 是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：

```python
>>> from collections import deque
>>> q = deque(['a', 'b', 'c'])
>>> q.append('x')
>>> q.appendleft('y')
>>> q
deque(['y', 'a', 'b', 'c', 'x'])
```

`deque` 除了实现list的 `append() `和 `pop()` 外，还支持 `appendleft()` 和 `popleft()` ，这 样就可以非常高效地往头部添加或删除元素。

- defaultdict

使用 `dict` 时，如果引用的Key不存在，就会抛出 `KeyError` 。如果希望key不存在时，返回一个默认值，就可以用 `defaultdict` ：

```python
>>> from collections import defaultdict
>>> dd = defaultdict(lambda: 'N/A')
>>> dd['key1'] = 'abc'
>>> dd['key1'] # key1存在
'abc'
>>> dd['key2'] # key2不存在，返回默认值
'N/A'
```

注意：默认值是调用函数返回的，而函数在创建 `defaultdict` 对象时传入。 除了在Key不存在时返回默认值， `defaultdict` 的其他行为跟 `dict` 是完全一样的。

- OrderedDict

使用 `dict` 时，Key是无序的。在对 `dict` 做迭代时，我们无法确定Key的顺序。 如果要保持Key的顺序，可以用 `OrderedDict` ：

```python
>>> from collections import OrderedDict
>>> d = dict([('a', 1), ('b', 2), ('c', 3)])
>>> d # dict的Key是无序的
{'a': 1, 'c': 3, 'b': 2}
>>> od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
>>> od # OrderedDict的Key是有序的
OrderedDict([('a', 1), ('b', 2), ('c', 3)])
```

注意， `OrderedDict` 的Key会按照插入的顺序排列，不是Key本身排序：

```python
>>> od = OrderedDict()
>>> od['z'] = 1
>>> od['y'] = 2
>>> od['x'] = 3
>>> list(od.keys()) # 按照插入的Key的顺序返回
['z', 'y', 'x']
```

利用 `OrderedDict` 可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key：

```python
from collections import OrderedDict

class FIFODict(OrderedDict):
    def __init__(self, capacity):
        super().__init__()
        self.capacity = capacity  # 最大容量

    def __setitem__(self, key, value):
        # 如果 key 已存在，先删除它（避免位置不对）
        if key in self:
            del self[key]
        # 插入新的键值对（会放在末尾）
        OrderedDict.__setitem__(self, key, value)
        # 如果超过容量，弹出最早插入的一个
        if len(self) > self.capacity:
            oldest = next(iter(self))  # 第一个键
            self.pop(oldest)
            
fifo = FIFODict(3)

fifo['a'] = 1
fifo['b'] = 2
fifo['c'] = 3
print(fifo)  # OrderedDict([('a', 1), ('b', 2), ('c', 3)])

fifo['d'] = 4  # 超过容量，自动删除最早的 'a'
print(fifo)  # OrderedDict([('b', 2), ('c', 3), ('d', 4)])
```

- ChainMap

`ChainMap` 可以把一组 `dict` 串起来并组成一个逻辑上的 `dict` 。 `ChainMap` 本身也是一个 `dict`，但是查找的时候，会按照顺序在内部的 `dict` 依次查找。

什么时候使用 `ChainMap` 最合适？举个例子：应用程序往往都需要传入参数，参数可以通过命令行传入，可以通过环境变量传入，还可以有默认参数。我们可以用 `ChainMap` 实现参数的优先级查找，即先查命令行参数，如果没有传入，再查环境变量，如果还是没有，就使用默认参数。

```python
from collections import ChainMap
import os, argparse

# 构造缺省参数:
defaults = {
 'color': 'red',
 'user': 'guest'
}

# 构造命令行参数:
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args()
command_line_args = { k: v for k, v in vars(namespace).items() if v }

# 组合成ChainMap:
combined = ChainMap(command_line_args, os.environ, defaults)

# 打印参数:
print('color=%s' % combined['color'])
print('user=%s' % combined['user'])
```

没有任何参数时，打印出默认参数：

```
D:\PythonProject\general>python use_chainmap.py
color=red
user=guest
```

传入命令行参数运行，优先使用命令行参数：

```
D:\PythonProject\general>python use_chainmap.py -u alice -c blue
color=blue
user=alice
```

传入环境变量运行：

```
D:\PythonProject\general>set user=bob

D:\PythonProject\general>set color=green

D:\PythonProject\general>python use_chainmap.py
color=green
user=bob
```

同时传入命令行参数和环境变量，命令行参数的优先级较高：

```
D:\PythonProject\general>set user=mike

D:\PythonProject\general>set color=pink

D:\PythonProject\general>python use_chainmap.py -u alice -c blue
color=blue
user=alice
```

##### 3. argparse

使用 `argparse` 解析参数，只需定义好参数类型，就可以获得有效的参数输入，能大大简化获取命令行参数的工作。

假设我们想编写一个备份MySQL数据库的命令行程序，需要输入的参数如下：

- host参数：表示MySQL主机名或IP，不输入则默认为 localhost ；
- port参数：表示MySQL的端口号，int类型，不输入则默认为 3306 ；
- user参数：表示登录MySQL的用户名，必须输入；
- password参数：表示登录MySQL的口令，必须输入；
- gz参数：表示是否压缩备份文件，不输入则默认为 False ；
- outfile参数：表示备份文件保存在哪，必须输入。

其中， `outfile` 是位置参数，而其他则是类似 `--user root` 这样的“关键字”参数。 

用 `argparse` 来解析参数，一个完整的示例如下：

```python
import argparse

def main():
    # 定义 ArgumentParser 实例
    parser = argparse.ArgumentParser(
        prog='backup',  # 程序名
        description='Backup MySQL database.',  # 描述
        epilog='Copyright (r), 2023'  # 说明信息
    )

    # 可选参数
    parser.add_argument('--host', default='localhost', help="主机名或 IP 地址")
    parser.add_argument('--port', default=3306, type=int, help="端口号")
    parser.add_argument('-u', '--user', required=True, help="用户名")
    parser.add_argument('-p', '--password', required=True, help="密码")
    parser.add_argument('--database', required=True, help="数据库名称")
    parser.add_argument('-gz', '--gzcompress', required=False, action='store_true', help='是否压缩备份文件 (.gz 格式)')

    # 位置参数（必须输入）
    parser.add_argument('outfile', help="备份文件保存路径")

    # 解析参数
    args = parser.parse_args()

    # 打印参数
    print('Parsed arguments:')
    print(f'outfile     = {args.outfile}')
    print(f'host        = {args.host}')
    print(f'port        = {args.port}')
    print(f'user        = {args.user}')
    print(f'password    = {args.password}')
    print(f'database    = {args.database}')
    print(f'gzcompress  = {args.gzcompress}')


if __name__ == '__main__':
    main()
```

输入有效的参数，则程序能解析出所需的所有参数：

```
D:\PythonProject\general>python backup.py -u root -p 123456 --database testdb backup.sql
Parsed arguments:
outfile     = backup.sql
host        = localhost
port        = 3306
user        = root
password    = 123456
database    = testdb
gzcompress  = False
```

缺少必要的参数，或者参数不对，将报告详细的错误信息：

```
D:\PythonProject\general>python backup.py --database testdb backup.sql
usage: backup [-h] [--host HOST] [--port PORT] -u USER -p PASSWORD --database DATABASE [-gz] outfile
backup: error: the following arguments are required: -u/--user, -p/--password
```

更神奇的是，如果输入 `-h` ，则打印帮助信息：

```
D:\PythonProject\general>python backup.py -h
usage: backup [-h] [--host HOST] [--port PORT] -u USER -p PASSWORD --database DATABASE [-gz] outfile

Backup MySQL database.

positional arguments:
  outfile               备份文件保存路径

options:
  -h, --help            show this help message and exit
  --host HOST           主机名或 IP 地址
  --port PORT           端口号
  -u, --user USER       用户名
  -p, --password PASSWORD
                        密码
  --database DATABASE   数据库名称
  -gz, --gzcompress     是否压缩备份文件 (.gz 格式)

Copyright (r), 2023
```

获取有效参数的代码实际上是这一行：

```python
args = parser.parse_args()
```

我们不必捕获异常， `parse_args()` 非常方便的一点在于，如果参数有问题，则它打印出错误信息后，结束进程；如果参数是 `-h` ，则它打印帮助信息后，结束进程。只有当参数全部有效时， 才会返回一个NameSpace对象，获取对应的参数就把参数名当作属性获取，非常方便。 

##### 4. base64

Base64 是一种编码方式，用于把二进制数据（比如图片、文件、字节流）转换成只包含 ASCII 字符的文本字符串。它接收一串 字节，把它编码成另一串字节，只是这串新字节中每个字节对应的是 ASCII 可打印字符。

Base64的原理很简单，首先，准备一个包含64个字符的数组：

```python
['A', 'B', 'C', ... 'a', 'b', 'c', ... '0', '1', ... '+', '/']
```

然后，对二进制数据进行处理，把3字节的二进制数据编码为4字节的文本数据，长度增加33%，好处是编码后的文本数据可以在邮件正文、网页等直接显示。

如果要编码的二进制数据不是3的倍数，最后会剩下1个或2个字节怎么办？Base64用 `\x00` 字节在末尾补足后，再在编码的末尾加上1个或2个 `=` 号，表示补了多少字节，解码的时候，会自动去掉。

Python内置的 `base64` 可以直接进行base64的编解码：

```python
>>> import base64
>>> base64.b64encode(b'hello world')
b'aGVsbG8gd29ybGQ='
>>> base64.b64decode(b'aGVsbG8gd29ybGQ=')
b'hello world'
```

由于标准的Base64编码后可能出现字符 `+` 和 `/` ，在URL中就不能直接作为参数，所以又有一种"url safe"的base64编码，其实就是把字符 `+` 和 `/` 分别变成 `-` 和 `_` ：

```python
>>> base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')
b'abcd++//'
>>> base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
b'abcd--__'
>>> base64.urlsafe_b64decode('abcd--__')
b'i\xb7\x1d\xfb\xef\xff'
```

Base64适用于小段内容的编码，比如数字证书签名、Cookie的内容等。

##### 5. struct

`struct` 模块是Python标准库中的一个 **用于在Python的数据类型（如整数、浮点数、字符串等）与 C语言风格的二进制数据之间进行转换** 的模块。

- 打包整数与浮点数

```python
>>> import struct
>>> data = struct.pack('i f s', 42, 3.14, b'A')
>>> data
b'*\x00\x00\x00\xc3\xf5H@A'
```

其中：`'i'` 表示一个 4 字节的整数 (int)，`'f'` 表示一个 4 字节的浮点数 (float)，`'s'` 表示一个字节串 (string)

- 解包二进制数据

```python
>>> import struct
>>> data = b'*\x00\x00\x00\xc3\xf5H@A'
>>> result = struct.unpack('i f s', data)
>>> result
(42, 3.140000104904175, b'A')
```

- 常用格式字符

| 格式字符 | 类型          | 字节大小   |
| -------- | ------------- | ---------- |
| `b`      | 有符号字符    | 1          |
| `B`      | 无符号字符    | 1          |
| `h`      | 短整型        | 2          |
| `H`      | 无符号短整型  | 2          |
| `i`      | 整型          | 4          |
| `I`      | 无符号整型    | 4          |
| `f`      | 浮点型        | 4          |
| `d`      | 双精度浮点型  | 8          |
| `s`      | 字符串        | 按长度决定 |
| `p`      | Pascal 字符串 | 按长度决定 |
| `?`      | 布尔值        | 1          |

- 字节序控制（大小端）

在格式字符串的开头可以指定字节序（endianness）：

| 前缀 | 含义               |
| ---- | ------------------ |
| `@`  | 本机字节序（默认） |
| `=`  | 本机标准字节序     |
| `<`  | 小端（低位在前）   |
| `>`  | 大端（高位在前）   |
| `!`  | 网络字节序（大端） |

Windows的位图文件（.bmp）是一种非常简单的文件格式，BMP格式采用小端方式存储数据，文件头的结构按顺序如下： 

两个字节： `'BM'` 表示Windows位图， `'BA'` 表示OS/2位图； 一个4字节整数：表示位图大小； 一个4字节整数：保留位，始终为0； 一个4字节整数：实际图像的偏移量； 一个4字节整数：Header的字节数； 一个4字节整数：图像宽度； 一个4字节整数：图像高度； 一个2字节整数：始终为1； 一个2字节整数：颜色数。

组合起来用 `unpack` 读取：

```python
>>> s = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'
>>> struct.unpack('<ccIIIIIIHH', s)
(b'B', b'M', 691256, 0, 54, 40, 640, 360, 1, 24)
```

结果显示， `b'B'` 、 `b'M'` 说明是Windows位图，位图大小为640x360，颜色数为24。

##### 6. hashlib

Python的 `hashlib` 提供了常见的哈希算法，如MD5，SHA1等等。

哈希算法通过哈希函数 `hash(data)` 对任意长度的数据 `data` 计算出固定长度的哈希 `digest` ，目的是为了发现原始数据是否被人篡改过。 哈希算法之所以能指出数据是否被篡改过，就是因为哈希函数是一个单向函数，计算 `digest=hash(data)` 很容易，但通过 `digest` 反推 `data` 却非常困难。而且，对原始数据做一个bit的修改，都会导致计算出的哈希完全不同。

MD5是最常见的哈希算法，速度很快，生成结果是固定的128 bit/16字节，通常用一个32位的16进制字符串表示：

```python
import hashlib

md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())	# d26a53750bc40b38b65a520292f69306
```

如果数据量很大，可以分块多次调用 `update()` ，最后计算的结果是一样的：

```python
import hashlib

md5 = hashlib.md5()
md5.update('how to use md5 in '.encode('utf-8'))
md5.update('python hashlib?'.encode('utf-8'))
print(md5.hexdigest())	# d26a53750bc40b38b65a520292f69306
```

另一种常见的哈希算法是SHA1，调用SHA1和调用MD5完全类似：

```python
import hashlib

sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())	# 2c76b57293ce30acef38d98f6046927161b46a44
```

SHA1的结果是160 bit/20字节，通常用一个40位的16进制字符串表示。

比SHA1更安全的算法是SHA256和SHA512，不过越安全的算法不仅越慢，而且哈希长度更长。

任何允许用户登录的网站都会存储用户登录的用户名和口令。如何存储用户名和口令呢？方法是存到数据库表中：

| **name** | **password** |
| -------- | ------------ |
| michael  | 123456       |
| bob      | abc789       |
| alice    | alice2025    |

如果以明文保存用户口令，如果数据库泄露，所有用户的口令就落入黑客的手里。此外，网站运维人员是可以访问数据库的，也就是能获取到所有用户的口令。这些都会有安全隐患。 正确的保存口令的方式是不存储用户的明文口令，而是存储用户口令的哈希，比如MD5：

| **name** | **password**                     |
| :------- | -------------------------------- |
| michael  | e10adc3949ba59abbe56e057f20f883e |
| bob      | 440cbbedf1e789ad49ac0969d2d8069a |
| alice    | 78d03b2810a74e5751c02db550798676 |

当用户登录时，首先计算用户输入的明文口令的MD5，然后和数据库存储的MD5对比，如果一致，说明口令输入正确，如果不一致，口令肯定错误。

采用MD5存储口令是否就一定安全呢？也不一定。假设你是一个黑客，已经拿到了存储MD5口令的数据库，如何通过MD5反推用户的明文口令呢？暴力破解费事费力，真正的黑客不会这么干。考虑这么个情况，很多用户喜欢用 123456 ， 888888 ， password 这些简单的口令，于是，黑客可以事先计算出这些常用口令的MD5值，得到一个反推表：

```python
hash_to_plain = {
 'e10adc3949ba59abbe56e057f20f883e': '123456',
 '21218cca77804d2ba1922c33e0151105': '888888',
 '5f4dcc3b5aa765d61d8327deb882cf99': 'password',
 '...': '...'
}
```

这样，无需破解，只需要对比数据库的MD5，黑客就获得了使用常用口令的用户账号。

对于用户来讲，当然不要使用过于简单的口令。但是，我们能否在程序设计上对简单口令加强保护呢？ 由于常用口令的MD5值很容易被计算出来，所以，要确保存储的用户口令不是那些已经被计算出来的常用口令的MD5，这一方法通过对原始口令加一个复杂字符串来实现，俗称“加盐”：

```python
def calc_md5(password):
    return get_md5(password + 'the-Salt')
```

经过Salt处理的MD5口令，只要Salt不被黑客知道，即使用户输入简单口令，也很难通过MD5反推明文口令。

但是如果有两个用户都使用了相同的简单口令比如 123456 ，在数据库中，将存储两条相同的MD5值，这说明这两个用户的口令是一样的。有没有办法让使用相同口令的用户存储不同的 MD5呢？ 如果假定用户无法修改登录名，就可以通过把登录名作为Salt的一部分来计算MD5，从而实现相同口令的用户也存储不同的MD5。

【小结】

哈希算法在很多地方都有广泛的应用。要注意哈希算法不是加密算法，不能用于加密（因为无法 通过哈希反推明文），只能用于防篡改，但是它的单向计算特性决定了可以在不存储明文口令的情况下验证用户口令。

##### 7. hmac

为了防止黑客通过彩虹表根据哈希值反推原始口令，在计算哈希的时候，不能仅针对原始输入计算，需要增加一个salt来使得相同的输入也能得到不同的哈希，这样，大大增加了黑客破解的难度。

如果salt是我们自己随机生成的，通常我们计算MD5时采用 md5(message + salt) 。但实际上，把salt看做一个“口令”，加salt的哈希就是：计算一段message的哈希时，根据不同口令计算出不同的哈希。要验证哈希值，必须同时提供正确的口令。这实际上就是Hmac算法：Keyed-Hashing for Message Authentication。它通过一个标准算 法，在计算哈希的过程中，把key混入计算过程中。

和我们自定义的加salt算法不同，Hmac算法针对所有哈希算法都通用，无论是MD5还是SHA1。采用Hmac替代我们自己的salt算法，可以使程序算法更标准化，也更安全。

Python自带的hmac模块实现了标准的Hmac算法，下面我们来看看如何使用hmac实现带key的哈希。

我们首先需要准备待计算的原始消息message，随机key，哈希算法，这里采用MD5，使用hmac的代码如下：

```python
>>> import hmac
>>> message = b'Hello, world!'
>>> key = b'secret'
>>> h = hmac.new(key, message, digestmod='MD5')
>>> # 如果消息很长，可以多次调用h.update(msg)
>>> h.hexdigest()
'fa4ee7d173f2d97ee79022d1a7355bcf'
```

可见使用hmac和普通hash算法非常类似。hmac输出的长度和原始哈希算法的长度一致。需要注意传入的key和message都是bytes类型，str类型需要首先编码为bytes。

【小结】

Python内置的hmac模块实现了标准的Hmac算法，它利用一个key对message计算“杂凑”后的hash，使用hmac算法比标准hash算法更安全，因为针对相同的message，不同的key会产生不同的hash。

##### 8. itertools

Python的内建模块 `itertools` 提供了非常有用的用于操作迭代对象的函数。

首先来看看 `itertools` 提供的几个“无限”迭代器：

- `count()` 会创建一个无限的迭代器

```python
>>> import itertools
>>> natuals = itertools.count(1)
>>> for n in natuals:
...     print(n)
...
1
2
3
...
```

- `cycle()` 会把传入的一个序列无限重复下去

```python
>>> import itertools
>>> cs = itertools.cycle('ABC') # 注意字符串也是序列的一种
>>> for c in cs:
... print(c)
...
'A'
'B'
'C'
'A'
'B'
'C'
...
```

- `repeat()` 负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数

```python
>>> ns = itertools.repeat('A', 3)
>>> for n in ns:
... print(n)
...
A
A
A
```

无限序列只有在 for 迭代时才会无限地迭代下去，如果只是创建了一个迭代对象，它不会事先把无限个元素生成出来，事实上也不可能在内存中创建无限多个元素。

无限序列虽然可以无限迭代下去，但是通常我们会通过 `takewhile()` 等函数根据条件判断来截取出一个有限的序列：

```python
>>> natuals = itertools.count(1)
>>> ns = itertools.takewhile(lambda x: x <= 10, natuals)
>>> list(ns)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

此外，`itertools` 提供的几个迭代器操作函数更加有用：

- `chain()` 可以把一组迭代对象串联起来，形成一个更大的迭代器：

```python
>>> import itertools
>>> for c in itertools.chain('ABC', 'XYZ'):
...     print(c)
...
A
B
C
X
Y
Z
>>>
```

- `groupby()` 把迭代器中相邻的重复元素挑出来放在一起：

```python
>>> import itertools
>>> for key, group in itertools.groupby('ABBCCCAAAA'):
...     print(key, list(group))
...
A ['A']
B ['B', 'B']
C ['C', 'C', 'C']
A ['A', 'A', 'A', 'A']
```

实际上挑选规则是通过函数完成的，只要作用于函数的两个元素返回的值相等，这两个元素就被认为是在一组的，而函数返回值作为组的key。如果我们要忽略大小写分组，就可以让元素 'A' 和 'a' 都返回相同的key：

```python
>>> import itertools
>>> for key, group in itertools.groupby('AaaBBbcCAAa', lambda x: x.upper()):
...     print(key, list(group))
...
A ['A', 'a', 'a']
B ['B', 'B', 'b']
C ['c', 'C']
A ['A', 'A', 'a']
```

【小结】

`itertools` 模块提供的全部是处理迭代功能的函数，它们的返回值不是list，而是Iterator，只有用for循环迭代的时候才真正计算。

##### 8. contextlib

Python的 `with` 语句允许我们非常方便地使用资源，而不必担心资源没有关闭：

```python
with open('/path/to/file', 'r') as f:
	f.read()
```

但并不是只有 `open()` 函数返回的fp对象才能使用 `with` 语句。实际上，任何对象，只要正确实现了上下文管理，就可以用于 `with` 语句。 实现上下文管理是通过 `__enter__` 和 `__exit__` 这两个方法实现的。例如，下面的class实现了这两个方法：

```python
class Query:
    def __init__(self, name):
        self.name = name
    def __enter__(self):
        print('Begain')
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print('Error')
        else:
            print('End')
    def query(self):
        print(f'Query info about {self.name}...')
```

这样，我们就可以把自己写的资源对象用于 `with` 语句：

```python
with Query('Bob') as q:
    q.query()
```

编写 `__enter__` 和 `__exit__` 仍然很繁琐，因此Python的标准库 `contextlib` 提供了更简单的写法，上面的代码可以改写如下：

```python
from contextlib import contextmanager

class Query(object):
    def __init__(self, name):
        self.name = name
    def query(self):
        print('Query info about %s...' % self.name)

@contextmanager
def create_query(name):
    print('Begin')
    q = Query(name)
    yield q
    print('End')

with create_query('Bob') as q:
    q.query()
```

`@contextmanager` 这个decorator接受一个generator，用 `yield` 语句把 `with ... as var` 把变量输出出去，然后， `with` 语句就可以正常地工作了。

很多时候，我们希望在某段代码执行前后自动执行特定代码，也可以用 `@contextmanager` 实现。例如：

```python
from contextlib import contextmanager
@contextmanager
def tag(name):
	print("<%s>" % name)
	yield
	print("</%s>" % name)

with tag("h1"):
	print("hello")
	print("world")
```

上面代码的执行结果为：

```python
<h1>
hello
world
</h1>
```

代码的执行顺序是：

1. `with` 语句首先执行 `yield` 之前的语句，因此打印出 `<h1>` ;
2. `yield` 调用会执行 `with` 语句内部的所有语句，因此打印出 `hello` 和 `world` ；
3. 最后执行 `yield` 之后的语句，打印出 `</h1>` 。

因此， `@contextmanager` 让我们通过编写generator来简化上下文管理。

##### 9. venv

`venv` 为应用提供了隔离的Python运行环境，解决了不同应用间安装多版本的冲突问题。

首先，我们假定要开发一个新的项目 `project01` ，需要一套独立的Python运行环境，可以这 么做： 

1. 创建目录，这里把Python虚拟运行环境命名为 `proj01env` ，因此目录名为 `proj01env` ：

```
$ mkdir proj01env
$ cd proj01env/
proj01env$
```

2. 创建一个独立的Python运行环境：

```
proj01env$ python3 -m venv .
```

查看当前目录，可以发现有几个文件夹和一个 `pyvenv.cfg` 文件：

```
proj01env$ ls
bin include lib pyvenv.cfg
```

命令 `python3 -m venv <目录>` 就可以创建一个独立的Python运行环境。观察 `bin` 目录的内容，里面有 `python3` 、 `pip3` 等可执行文件，实际上是链接到Python系统目录的软链接。

3. 继续进入 `bin` 目录，Linux/Mac用 `source activate` ，Windows用 `activate.bat` 激活该venv环境：

```
proj01env$ cd bin
bin$ source activate
(pro101env) bin$
```

注意到命令提示符变了，有个 `(proj01env)` 前缀，表示当前环境是一个名为 `proj01env` 的 Python环境。

4. 下面正常安装各种第三方包，并运行 `python` 命令：

```
(proj101env) bin$ pip3 install jinja2
...
Successfully installed jinja2-xxx
(proj101env) bin$ python3
>>> import jinja2
>>> exit()
```

在 `venv` 环境下，用 `pip` 安装的包都被安装到 `proj01env` 这个环境下，具体目录是 `proj01env/lib/python3.x/site-packages` ，因此，系统Python环境不受任何影响。也就是说， `proj01env` 环境是专门针对 `project01` 这个应用创建的。 

5. 退出当前的 `proj01env` 环境，使用 `deactivate` 命令：

```
(proj101env) bin$ deactivate
bin$
```

此时就回到了正常的环境，现在继续 `pip` 或 `python` 均是在系统Python环境下执行。

### 常用第三方模块

##### 1. Pillow

PIL：Python Imaging Library，已经是Python平台事实上的图像处理标准库了。PIL功能非常强大，但API却非常简单易用。 由于PIL仅支持到Python 2.7，加上年久失修，于是一群志愿者在PIL的基础上创建了兼容的版本，名字叫Pillow，支持最新Python 3.x，又加入了许多新特性。

`PIL` 提供了操作图像的强大功能，可以通过简单的代码完成复杂的图像处理：

- 安装 Pillow

```bash
pip install Pillow
```

- 打开和显示图片： `open()` 和 `show()`

```python
from PIL import Image

# 打开图片
img = Image.open("example.jpg")

# 显示图片
img.show()

# 查看基本信息
print(img.format, img.size, img.mode)
```

- 保存图片： `save()`

```python
img.save("output.png")  # 保存为PNG格式
```

- 图像格式转换： `convert()`

```python
img = Image.open("example.jpg")
img.convert("L").save("gray.png")  # 转换为灰度图
```

其他功能如切片、旋转、滤镜、输出文字、调色板等一应俱全。

##### 2. Requests

`requests` 是Python中最常用、最优雅的HTTP网络请求库之一，广泛用于网页爬取、API调用、接口测试等场景。

- 发送GET请求：

```python
import requests

response = requests.get("https://api.github.com")
print(response.text)
```

对于带参数的URL，传入一个字典作为参数：

```python
>>> r = requests.get('https://www.douban.com/search', params={'q':'python','cat':'1001'})
>>> r.url
'https://www.douban.com/search?q=python&cat=1001'
```

- 发送POST请求：

```python
login_data = {"username": "admin", "password": "123456"}
response = requests.post("https://example.com/login", data=login_data)
```

`requests` 默认使用 `application/x-www-form-urlencoded` 对POST数据编码。如果要传递JSON数据，可以直接传入json参数：

```python
my_data = {'key': 'value'}
r = requests.post(url, json=my_data) # 内部自动序列化为JSON
```

类似的，如果要上传文件，这将需要更复杂的编码格式，但是 `requests` 把它简化成 `files` 参数：

```python
files = {"file": open("test.png", "rb")}
r = requests.post("https://example.com/upload", files=files)
```

注意，在读取文件时，务必使用 '`rb'` 即二进制模式读取，这样获取的字节长度才是文件的长度。

此外，把 `post()` 方法替换为 `put()` ， `delete()` 等，就可以以PUT或DELETE方式请求资源。

- 一些常用参数：

| 参数      | 说明                                          | 示例                                                         |
| --------- | --------------------------------------------- | ------------------------------------------------------------ |
| `params`  | URL 查询参数                                  | `requests.get(url, params={"q": "python"})`                  |
| `data`    | 表单数据（application/x-www-form-urlencoded） | `requests.post(url, data={"key":"value"})`                   |
| `json`    | 发送 JSON 数据                                | `requests.post(url, json={"name": "GPT"})`                   |
| `headers` | 自定义请求头                                  | `requests.get(url, headers={"User-Agent": "MyApp"})`         |
| `cookies` | 发送 cookies                                  | `requests.get(url, cookies={"sessionid": "abc123"})`         |
| `timeout` | 超时时间（秒）                                | `requests.get(url, timeout=5)`                               |
| `proxies` | 使用代理                                      | `requests.get(url, proxies={"http": "http://127.0.0.1:8080"})` |

- 获取响应内容

```python
r = requests.get("https://jsonplaceholder.typicode.com/todos/1")

print(r.text)        # 原始文本
print(r.json())      # 解析为 JSON 对象
print(r.status_code) # 状态码
print(r.url)         # 最终 URL
print(r.headers)     # 响应头
```

##### 3. chardet

`chardet` 的作用是自动检测文本的字符编码。当我们拿到一个 字节串(bytes) 时，就可以对其检测编码。

```python
>>> chardet.detect(b'Hello, world!')
{'encoding': 'ascii', 'confidence': 1.0, 'language': ''}
```

检测出的编码是 `ascii` ，注意到还有个 `confidence` 字段，表示检测的概率是1.0（即100%）。

再来试试检测GBK编码的中文：

```python
>>> data = '离离原上草，一岁一枯荣'.encode('gbk')
>>> chardet.detect(data)
{'encoding': 'GB2312', 'confidence': 0.7407407407407407, 'language':
'Chinese'}
```

检测的编码是 `GB2312` ，注意到GBK是GB2312的超集，两者是同一种编码，检测正确的概率是74%，`language` 字段指出的语言是 `'Chinese'` 。

再试试对日文进行检测：

```python
>>> data = '最新の主要ニュース'.encode('euc-jp')
>>> chardet.detect(data)
{'encoding': 'EUC-JP', 'confidence': 0.99, 'language': 'Japanese'}
```

可见，用 `chardet` 检测编码，使用简单。获取到编码后，再转换为 `str `，就可以方便后续处理。

### 网络编程

##### 1. TCP/IP简介

虽然大家现在对互联网很熟悉，但是计算机网络的出现比互联网要早很多。 

计算机为了联网，就必须规定通信协议，早期的计算机网络，都是由各厂商自己规定一套协议， IBM、Apple和Microsoft都有各自的网络协议，互不兼容，这就好比一群人有的说英语，有的说中文，有的说德语，说同一种语言的人可以交流，不同的语言之间就不行了。

为了把全世界的所有不同类型的计算机都连接起来，就必须规定一套全球通用的协议，为了实现互联网这个目标，互联网协议簇（Internet Protocol Suite）就是通用协议标准。Internet是由inter和net两个单词组合起来的，原意就是连接“网络”的网络，有了Internet，任何私有网络，只要支持这个协议，就可以联入互联网。 

因为互联网协议包含了上百种协议标准，但是最重要的两个协议是TCP和IP协议，所以，大家把互联网的协议简称TCP/IP协议。

通信的时候，双方必须知道对方的标识，好比发邮件必须知道对方的邮件地址。互联网上每个计算机的唯一标识就是IP地址，类似 123.123.123.123 。如果一台计算机同时接入到两个或更多的网络，比如路由器，它就会有两个或多个IP地址，所以，IP地址对应的实际上是计算机的网络接口，通常是网卡。

IP协议负责把数据从一台计算机通过网络发送到另一台计算机。数据被分割成一小块一小块，然后通过IP包发送出去。由于互联网链路复杂，两台计算机之间经常有多条线路，因此，路由器就负责决定如何把一个IP包转发出去。IP包的特点是按块发送，途径多个路由，但不保证能到达， 也不保证顺序到达。

IP地址实际上是一个32位整数（称为IPv4），以字符串表示的IP地址如 192.168.0.1 实际上是 把32位整数按8位分组后的数字表示，目的是便于阅读。

IPv6地址实际上是一个128位整数，它是目前使用的IPv4的升级版，以字符串表示类似于 2001:0db8:85a3:0042:1000:8a2e:0370:7334 。

TCP协议则是建立在IP协议之上的。TCP协议负责在两台计算机之间建立可靠连接，保证数据包按顺序到达。TCP协议会通过握手建立连接，然后，对每个IP包编号，确保对方按顺序收到，如果包丢掉了，就自动重发。许多常用的更高级的协议都是建立在TCP协议基础上的，比如用于浏览器的HTTP协议、发送邮件的SMTP协议等。

一个TCP报文除了包含要传输的数据外，还包含源IP地址和目标IP地址，源端口和目标端口。 

端口有什么作用？在两台计算机通信时，只发IP地址是不够的，因为同一台计算机上跑着多个网络程序。一个TCP报文来了之后，到底是交给浏览器还是QQ，就需要端口号来区分。每个网络程序都向操作系统申请唯一的端口号，这样，两个进程在两台计算机之间建立网络连接就需要各自的IP地址和各自的端口号。一个进程也可能同时与多个计算机建立链接，因此它会申请很多端口。

了解了TCP/IP协议的基本概念，IP地址和端口的概念，我们就可以开始进行网络编程了。

