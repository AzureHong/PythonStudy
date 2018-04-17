def say_hello():
    # 该函数块的主要内容
    print('Hello world 真的是所有的都从这里开始')
    # 函数块完结

say_hello()

# 可变参数
def total(a = 5, *numbers,**phonebook):
    print('a',a)
    print('phonebook',phonebook)

    # 遍历元组中所有项目
    for single_item in numbers:
        print('single_item',single_item)

   

print(total(10,1,2,3,Jack=1123,John=2231,Inge=1560))