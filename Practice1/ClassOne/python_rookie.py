#coding=utf-8
# 菜鸟驿站的基础习题练习
# 1. Hello Wrold 实例
print('Hello World')

'''
# 2. 数字求和
num1 = input("请输入第一个数字")
num2 = input("请输入第二个数字")

sum = float(num1)+float(num2)
print('数字{} 和{} 相加结果为：{}'.format(num1,num2,sum))
'''
# 3. 平方根
'''
# 第一种实现方式
num = float(input('请输入一个数字'))
sqrt = num ** 0.5
print(' %0.3f 的平方根为 %0.3f'%(num ,sqrt))

#第二种实现方式
import cmath
 
num = int(input("请输入一个数字: "))
num_sqrt = cmath.sqrt(num)
print('{0} 的平方根为 {1:0.3f}+{2:0.3f}j'.format(num ,num_sqrt.real,num_sqrt.imag))
'''


# 嵌套IF
'''
num = float(input('请输入一个数字'))

if num>=0:
    if num == 0:
        print('零')
    else:
        print('正数')
else:
    print('负数')
'''

# 判断字符串是否为数字
import unicodedata

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    
    try:
        unicodedata.numeric(s)
        return True
    except(TypeError,ValueError):
        pass
    return False

    # Python中 isdigit() 方法检测字符串是否只由数字组成。
    # Python isnumeric() 方法检测字符串是否只由数字组成。这种方法是只针对unicode对象。
    # 测试字符串和数字
print(is_number('foo'))   # False
print(is_number('1'))     # True
print(is_number('1.3'))   # True
print(is_number('-1.37')) # True
print(is_number('1e3'))   # True
 
# 测试 Unicode
# 阿拉伯语 5
print(is_number('٥'))  # True
# 泰语 2
print(is_number('๒'))  # True
# 中文数字
print(is_number('四')) # True
# 版权号
print(is_number('©'))  # False