# -*- coding: utf-8 -*- 
# knowledge_summer

'''
原地交换两个数字
'''
x, y = 1, 3
x, y = y, x
print(x, y)
#3 1

'''
链式比较运算
'''
n = 10
result = 1 < n < 20
print(result)
#True

'''
三目运算符
value1 if condition else value2
classA if condition else classB(param...)
'''
n = 10 if True else 20
print(n)
#10

mstr = "line1"\
       "line2"
mstr_ = '''line1
line2'''
print(mstr_)

ll = [1, 2, 3]
x, y, z = ll
print(x, y, z)
#1, 2, 3
#变长参数 可为空
def mprint(*ll, **dd):
    print(type(ll), ll)
    print(type(dd), dd)
    pass
mprint(1, 2, 3, 4, key1=3, key2=5)
#<class 'tuple'> (1, 2, 3, 4)
#<class 'dict'> {'key1': 3, 'key2': 5}
#note: len(tuple) == 1时 tuple定义
tt = 1,
print(type(tt))

'''
如果你想知道引用到代码中模块的绝对路径，可以使用下面的技巧：

import threading
import socket
 
print(threading)
print(socket)
 
#1- <module 'threading' from '/usr/lib/python2.7/threading.py'>
#2- <module 'socket' from '/usr/lib/python2.7/socket.py'>
'''

'''
这是一个我们大多数人不知道的有用特性，在 Python 控制台，不论何时我们测试一个表达式或者调用一个方法，结果都会分配给一个临时变量： _（一个下划线）。

>>> 2 + 1
3
>>> _
3
>>> print _
3

“_” 是上一个执行的表达式的输出。
'''

testDict = {i: i * i for i in range(10)}
testSet = {i * 2 for i in range(10)}
print(testDict, testSet)

#buildin function
ll = []
print(dir(ll))
print(ll.__dir__())

#if m in [1,3,5,7]:

'''
当正在运行的 Python 低于支持的版本时，有时我们也许不想运行我们的程序。为达到这个目标，你可以使用下面的代码片段，它也以可读的方式输出当前 Python 版本：

import sys
 
#Detect the Python version currently in use.
if not hasattr(sys, "hexversion") or sys.hexversion != 50660080:
    print("Sorry, you aren't running on Python 3.5n")
    print("Please upgrade to 3.5.n")
    sys.exit(1)
 
#Print Python version in a readable format.
print("Current Python version: ", sys.version)

或者你可以使用 sys.version_info >= (3, 5) 来替换上面代码中的 sys.hexversion != 50660080，这是一个读者的建议。

在 Python 2.7 上运行的结果：

Python 2.7.10 (default, Jul 14 2015, 19:46:27)
[GCC 4.8.2] on linux
 
Sorry, you aren't running on Python 3.5
 
Please upgrade to 3.5.

在 Python 3.5 上运行的结果：

Python 3.5.1 (default, Dec 2015, 13:05:11)
[GCC 4.8.2] on linux
 
Current Python version:  3.5.2 (default, Aug 22 2016, 21:11:05)
[GCC 5.3.0]
'''

test = ['I', 'Like', 'Python', 'automation']
print(''.join(test))

ll = [1, 2, 3]
ll.reverse()
print(ll)
print(ll[::-1])


ll = [i for i in range(5, 15)]
for i, v in enumerate(ll):
    print(i, ":", v)

import enum
class ConstValue(enum.IntEnum):
    one = 1
print(ConstValue.one, 1 == ConstValue.one)


def func():
    return 1, 2, 3, 4



import functools
ll = [1, 2, 3, 4]
print(functools.reduce(lambda x,y:x+y, ll))
[print(i) for i in map(lambda x:x**2, ll)]    
print(ll)

nfunc = functools.partial(lambda x,y:x+y, 1)
print(nfunc(2))

test = [1,2,3,4,2,2,3,1,4,4,4]
print(max(set(test), key=test.count))
for i in test:
    print(test.count(i))


'''
Python 限制递归次数到 1000，我们可以重置这个值：

import sys
 
x=1001
print(sys.getrecursionlimit())
 
sys.setrecursionlimit(x)
print(sys.getrecursionlimit())
 
#1-> 1000
#2-> 1001

请只在必要的时候采用上面的技巧。
'''

import sys
x=1
print(sys.getsizeof(x))

'''
import sys
class FileSystem(object):
 
    def __init__(self, files, folders, devices):
        self.files = files
        self.folders = folders
        self.devices = devices
print(sys.getsizeof( FileSystem ))
 
class FileSystem1(object):
 
    __slots__ = ['files', 'folders', 'devices']
    def __init__(self, files, folders, devices):
        self.files = files
        self.folders = folders
        self.devices = devices
 
print(sys.getsizeof( FileSystem1 ))
#In Python 3.5
#1-> 1016
#2-> 888
'''

t1 = (1, 2, 3)
t2 = (10, 20, 30) 
print(dict(zip(t1,t2)))
print(dict([(1,10), (2,10), (3,30)]))

import itertools
test = [[-1, -2], [30, 40], [25, 35]]
print(list(itertools.chain.from_iterable(test)))



def xswitch(x):
    return xswitch._system_dict.get(x, None) 
xswitch._system_dict = {'files': 10, 'folders': 5, 'devices': 2} 
print(xswitch('default'))
print(xswitch('devices')) 
#1-> None
#2-> 2


#生成器
def mpow():
    i = 0
    while True:
        print('-----', i)
        yield i**2
        i+=1        
        if i==10:
            raise StopIteration
#生成器
try:
    cc = mpow()
    while True:
        print(next(cc))
except BaseException as e:#except StopIteration as e:?????????????
    print("-----StopIteration-----")

'''
cc = mpow()
for i in cc:
    print(i)
'''

#迭代器
class MyList:
    def __init__(self, *values):
        self.__ll = values
        self.__index = -1
        print(self.__ll)
    def __next__(self):
        print('__next__')
        self.__index += 1
        if self.__index == len(self.__ll):
            raise StopIteration
        return self.__ll[self.__index]
        pass
    def __iter__(self):
        print('__iter__')
        return self
    def __getitem__(self, key):
        print('__getitem__')
        return self.__ll[key]
    def __getattr__(self, key):
        index = int(key)
        return self.__ll[index]

mll = MyList(1, 2, 3, 4, 5)
for i in mll:
    print(i)
for i in range(len(mll._MyList__ll)):
    print(mll[i])
for i in range(len(mll._MyList__ll)):
    print(mll[str(i)])

#装饰器
def decorate_1(func):
    print("装饰器_1", func.__name__)
    return func

def decorate_2(func):
    print("装饰器_2", func.__name__)
    def __func(*list_, **dict_):
        print("装饰器_2", __func.__name__)
        return func(*list_, **dict_)
    return __func

@decorate_1
def add(x, y):
    return x+y
print(add(1, 1))

@decorate_2
def add(x, y):
    return x+y
print(add(1, 1))

