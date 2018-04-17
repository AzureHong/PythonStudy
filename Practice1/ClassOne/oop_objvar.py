# 类变量与对象变量
# 类变量：共享特性，可以被属于该类的所有实例访问，只有一个副本，当任何一个对象对类变量做出改变时，发生的变动将在其它所有的实例中都会得到体现
# 对象变量：由每个独立的对象或实例拥有，不被共享，也不会以任何方式与其它不同实例中相同名称的字段产生关联，每个对象都拥有属于它自己的字段副本

# coding=UTF-8
class Robot:
    """表示有一个带有名字的机器人。"""
# 一个类变量，用来计数机器人的数量
    population = 0
    def __init__(self, name):
        """初始化数据"""
        self.name = name
        print("(Initializing {})".format(self.name))
        # 当有人被创建时，机器人
        # 将会增加人口数量
        Robot.population += 1

    def die(self):
        """我挂了。"""
        print("{} is being destroyed!".format(self.name))
        Robot.population -= 1
        if Robot.population == 0:
            print("{} was the last one.".format(self.name))
        else:
            print("There are still {:d} robots working.".format(Robot.population))

    def say_hi(self):
        """来自机器人的诚挚问候
            
            没问题，你做得到。"""
        print("Greetings, my masters call me {}.".format(self.name))
    @classmethod
    def how_many(cls):
        """打印出当前的人口数量"""
        print("We have {:d} robots.".format(cls.population))

droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()
droid2 = Robot("C-3PO")
droid2.say_hi()
Robot.how_many()
print("\nRobots can do some work here.\n")
print("Robots have finished their work. So let's destroy them.")
droid1.die()
droid2.die()
Robot.how_many()