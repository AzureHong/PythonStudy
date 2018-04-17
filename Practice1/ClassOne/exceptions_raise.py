# raise抛出异常 ：提供错误名或异常名以及要抛出的异常的对象
# encoding=UTF-8
class ShortInputException(Exception):
    '''一个由用户定义的异常类'''
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast
    
try:
    text = input('Enter something --> ')
    if len(text) < 3:
        raise ShortInputException(len(text), 3)
    # 其他工作能在此处继续正常运行
except EOFError:
    print('Why did you do an EOF on me?')
except ShortInputException as ex:
    print(('ShortInputException: The input was ' + '{0} long, expected at least {1}').format(ex.length, ex.atleast))
else:
    print('No exception was raised.')

# 在try块中获取资源，然后在finally块中释放资源是一种常见模式，使用with可以使这一过程可以以一种干净的姿态得以完成

with open("poem.txt") as f:
    for line in f:
        print(line, end='')

# 此模式下，with open会自动完成关闭文件的操作