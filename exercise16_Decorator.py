"""
import time
import functools

def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = fn(*args, **kwargs)
        end = time.time()
        elapsed_ms = (end - start) * 1000
        print('%s executed in %.3f ms' % (fn.__name__, elapsed_ms))
        return result
    return wrapper

# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z

f = fast(11, 22)
s = slow(11, 22, 33)

"""
"""
import functools

def decorator(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        print('begain call')
        result = fn(*args, **kwargs)
        print('end call')
        return result
    return wrapper

@decorator
def say_nihao():
    print('nihao~')

say_nihao()
"""
import functools

def log(text=None):
    # 情况1：@log  —> text 是函数
    if callable(text):
        func = text
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print(f"调用 {func.__name__}():")
            return func(*args, **kw)
        return wrapper
    
    # 情况2：@log() 或 @log("xxx") —> text 是 None 或字符串
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            msg = text if text else "调用"
            print(f"{msg} {func.__name__}():")
            return func(*args, **kw)
        return wrapper
    return decorator

@log
def say_nihao():
    print('nihao~')
    
@log()
def say_hi():
    print('nihao~')

@log('好好好，快调用')
def say_hello():
    print('nihao~')


say_nihao()
say_hi()
say_hello()

