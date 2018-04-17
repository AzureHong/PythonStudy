# Python流程控制练习

# 在迭代过程中修改迭代序列不安全（只有在使用链表这样的可变序列时才会有这样的情况）
# 可以使用切割标识来进行：注意其用法，下标标定，正负倒序
'''
words = ['cat','window','defenestrate','others']

for w in words[:]:
    print(w,len(w))
'''

# 在不同方面range()函数返回的对象表现为它是一个列表，但事实上它并不是，当你迭代它时，它是一个能够像期望的序列返回连续项的对象，但是为了节省空间，它并不真正构造列表
# print(list(range(5))) 


# for 与 else 的联用，代表for循环完成或执行条件为false（与while联用时）时执行
'''
for n in range(2,10):
    for x in range(2,n):
        if n % x == 0:
            print(n,'equals',x,'*',n/x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')
'''

# 默认值只能被赋值一次，这使得当默认值是可变对象时会有所不同，比如列表、字典或大多数据类的实例
# 示例： 函数在后续调用过程中会累积（前面）传给他的参数
'''
def f(a,l=[]):
    
    if l is None: # 避免调用中参数累积，在使用默认之情况下，归档
        l = []
    l.append(a)
    return l

print(f(1))
print(f(2))
print(f(3))
'''

# 在函数调用中，关键字的参数必须跟在位置参数的后面，传递的所有关键字参数必须与函数接受的某个参数相匹配
# lambda 返回一个函数，可以将小函数作为参数传递
'''
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair:pair[1])
print(pairs)
'''

# 注解是以字典形式存储在函数中的__annotations__属性中，对函数的其它部分没有任何影响
# 使用方式：-> 表达式 ：


# Python PEP8风格
# 类名：驼峰命名
# 函数和方法： 小写_和_下划线，self总是作为方法的第一个参数

# list 方法集合

# Python 中对所有可变的数据类型，insert、remove、sort 返回None
'''
# list 列表方法使得列表可以很方便的作为一个堆栈来使用，特性：先进后出
# append() 可以将元素添加到堆栈定，用不指定索引的pop()可以将元素从堆栈定中释放出来
# deque 双端队列包
# 队列 先进先出
'''

'''
    推导式：即解析式，是Python的一种独有特性，推导式是可以从一个数据序列构建另一个新的数据序列的结构体
    1. 列表推导式 List
    2. 字典推导式 Dict
    3. 集合推导式 Set

    1) 列表推导式 基本语法

    res = [out_exp_res for out_ext in input_list if out_exp == 2]
    out_exp_res:　　列表生成元素表达式，可以是有返回值的函数。
    for out_exp in input_list：　　迭代input_list将out_exp传入out_exp_res表达式中。
    if out_exp == 2：　　根据条件过滤哪些值可以。
    汉化版本： res = [列表生成的元素表达式 for 迭代结果 in 被迭代list if 迭代结果的过滤条件]
    
'''

'''
# list推导式示例1
multiples = [i for i in range(30) if i % 3 is 0]
print(multiples)

# list推导式示例2
def squared(x):
    return x * x

multiples = [squared(i) for i in range(30) if i % 3 is 0]
print(multiples)
'''

'''
# Dict推导式，模式同列表推导式类似，将[] 修改为 {}
# 将Key大小写合并
mcase = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}
mcase_frequency = {
    k.lower(): mcase.get(k.lower(), 0) + mcase.get(k.upper(), 0) 
    for k in mcase.keys() 
    if k.lower() in ['a','b']
}
print(mcase_frequency)
'''

'''
# 集合推导式，同list推导式类似，使用{}
squares = {x**2 for x in [1,1,2]}
print(squares)
'''

'''
    # 题目：创建list，下列三种方式结果等价
squares = []
for x in range(10):
    squares.append(x**2)
print(squares)

squares = list(map(lambda x:x**2,range(10)))
print(squares)

squares = [x**2 for x in range(10)]
print(squares)
'''

'''
# 嵌套的列表推导式 矩阵行转列
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
matrix = [[row[i] for row in matrix] for i in range(4)]
print(matrix)

# 等价于
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print(transposed)
'''

# 重要：在实际中，内置函数组成复杂流程语句，推荐使用zip()函数

'''
# Set 无序不重复元素集，基本功能包括关系测试和消除重复元素，集合对象支持：联合、交、差、对称差集等数学运算
# 注意：创建空集合必须使用set() ，而不是{}
a = set('abracadabra')
b = set('alacazam')
print(a)
# 输出结果{'a', 'r', 'b', 'c', 'd'}
# a-b 交集，a | b,a & b ,a ^ b
print(a - b)
print(a | b)
print(a & b)
print(a ^ b)
'''

# 字典：某些情况下可以称之为联合内存 或联合数组，字典是以关键字为索引
# 序列：是以连续的整数位索引
# 最佳理解角度：可以视为无序的键-值对的集合
# dict()构造函数可以直接从key-value对中创建字典
# 示例 dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
#      dict(sape=4139, guido=4127, jack=4098)
# 字典推导式，示例：{x:x**2 for x in (2,4,6)}

'''
# 字典：关键字和对应的值可以使用items()解读出来
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k,v in knights.items():
    print(k,v)

# lsit中 enumerate() 函数，获取索引位置，和对应的值
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i,v)

# zip()可以做整体打包,同时循环两个或更多的序列
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q,a in zip(questions,answers):
    print('What is you {}? It is {}.'.format(q,a))

# 逆向循环：首先正向定位序列，然后使用reversed() 函数
for i in reversed(range(1, 10, 2)):
    print(i)

# 按照排序后的顺序循环序列，推荐使用sorted() 它不改动原序列，会生成一个新的已排序的序列
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)
'''

# 比较操作符可以传递，如 a <b == c ，审核是否a小于b，且b等于c
# 逻辑操作符，not具备最高优先级，or级别最低,and 和 or 是短路操作符

###################### 模块#######################
# dic() 函数，用于按模块名搜索模块定义，它返回一个字符串类型的存储列表，无参时候，返回变量、模块、韩式等

# 预定义清理行为 with
# 无论对象操作是否成功，不再需要该对象的时候就会起作用

'''
class Complex:
    def __init__(self,realpart,imagpart):
        print(self)
        #print(realpart)
        #print(imagpart)
        self.r = realpart
        self.i = imagpart
    
x = Complex(3,-5)
print(x.r)
'''

# 类迭代器，定义__iter__() 和__next__() 如果当前类定义了__next__()方法，只需要在 __iter__()中返回self

# 线程是一个分离无顺序依赖关系任务的技术，在某些任务运行于互殴太的时候，应用程序会变得迟缓，线程可以提升其速度。
# 另一个有关用途：在I/O的同时其它线程可以并行计算
# threading 模块
'''
import threading, zipfile

class AsyncZip(threading.Thread):
    def __init__(self, infile, outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile
    def run(self):
        f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close()
        print('Finished background zip of:', self.infile)

background = AsyncZip('mydata.txt', 'myarchive.zip')
background.start()
print('The main program continues to run in foreground.')

background.join()    # Wait for the background task to finish
print('Main program waited until background was done.')

'''

# 推荐方法，任务协调的首选方法是把对一个资源的所有访问集中在一个单独的线程中，然后使用queue模块用那个线程服务其他线程的请求。
# 为了内部线程通信和协调而使用Queue对象的应用程序更易于设计、可读和可靠

# 弱引用 weakref模块，提供了不用创建引用的跟踪对象工具，一旦对象不再存在，它自动从弱引用表上删除并触发回调。典型应用：捕获难以构造的对象

# decimal 提供了Decimal数据类型用于浮点数计算，例如十进制

# fractions 模块支持另一种形式的运算，它实现的运算基于有理数，可以1/3这样的数字可以精确的标识

# 如果是浮点数操作的重度使用者，可以使用SciPy项目提供的Numerical Python 包和其它用于数学和统计学的包
