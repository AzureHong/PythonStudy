
# 我会推荐你总是使用括号，来指明元组的开始于结束，尽管其是一个可选项
# 原则：明了胜过晦涩，显式优于隐式

# 元组同时也是一个序列

zoo = ('Python','elephant','penguin')
print('Number of animals in the zoo is',len(zoo))

new_zoo = 'monkey','camel',zoo
print('Nmuber of cages in the new zoo is',len(new_zoo))
print('All animals in new zoo are',new_zoo)
print('Animals brought from old zoo is',new_zoo[2])
print('Last animals brought from old zoo is ',new_zoo[2][2])
print('Number of animals in the new zoo is',len(new_zoo)-1+len(new_zoo[2]))

# 在同一个函数中返回两个不同的值，可以使用元组
# a,b = <some expression>的用法会将表达式的结果解释为一个具有两个值的元组
def get_error_details():
    return (2,'details')

errnum,errstr = get_error_details()
print('errnum:',errnum)
print('errstr:',errstr)


# 这也意味着，在Python中交换两个变量最快的方法是使用此种变量方式
a = 5;b = 8
print('a=',a)
print('b=',b)

a,b = b,a
print('a=',a)
print('b=',b)



