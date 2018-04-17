# lambda 表格，lambda语句可以创建一个新的函数对象，模式lambda 参数：表达式
points = [{'x': 2, 'y': 3},{'x': 4, 'y': 1}]

points.sort(key=lambda i:i['y'])
print(points)

# 详细解释：自定义排序，为此我们需要一个函数，但是又不为函数编写独立的def块，只在这一个地方使用，此时可以使用lambda表达式来创建一个新函数


# 列表推导：用于从一份现有的列表中得到一份新列表
# 优点：当我们使用循环来处理列表中的每个元素并将其存储到新的列表中时，它能减少样板代码的数量
listone = [2,3,4]
listtwo = [2*i for i in listone if i>2]
print(listtwo)

# 在函数中接收元组与字典
# *args 使用*前缀，函数的所有其它的额外参数都将传递到args中，并作为一个元组予以存储
# **args 使用**前缀，额外的参数都将被视为字典的键值对

def powersum(power,*args):
    '''Return the sum of each argument raised to the specified power.'''
    total = 0
    for i in args:
        total +=pow(i,power)
    return total

print(powersum(2,3,4))
print(powersum(2,10))

# assert 断言，断言某事为真，如果确认则继续，如果失败则抛出异常 AssertionError
# 需要明智选择，在大多数情况下，它好过捕获异常，也好过定位问题或向用户显示错误信息然后退出

# 装饰器Decorators 应用包装函数的快捷方式，有助于将某一功能与一些代码一遍又一遍的进行“包装”
