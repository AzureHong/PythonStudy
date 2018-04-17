# __init__ 会在类的对象被实例化时立即运行，这一方法可以对任何你想要进行操作的目标对象进行初始化操作

class Person:
    def __init__(self,name):
        self.name = name
    
    def say_hi(self):
        print('Hello , my name is ', self.name)

p = Person('Swaroop')
p.say_hi()

