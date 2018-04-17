# 序列：主要功能是资格测试，即in、not in、索引操作等，它能够允许我们直接获取序列中的特定项目

# 索引操作使用负数，在这种情况下，位置计数将从队列的末尾开始

shoplist = ['apple', 'mango', 'carrot', 'banana']
name = 'swaroop'
# Indexing or 'Subscription' operation #
# 索引或“下标（Subscription）”操作符 #
print('Item 0 is', shoplist[0])
print('Item 1 is', shoplist[1])
print('Item 2 is', shoplist[2])
print('Item 3 is', shoplist[3])
print('Item -1 is', shoplist[-1])
print('Item -2 is', shoplist[-2])
print('Character 0 is', name[0])
# Slicing on a list #
print('Item 1 to 3 is', shoplist[1:3])
print('Item 2 to end is', shoplist[2:])
print('Item 1 to -1 is', shoplist[1:-1])
print('Item start to end is', shoplist[:])
# 从某一字符串中切片 #
print('characters 1 to 3 is', name[1:3])
print('characters 2 to end is', name[2:])
print('characters 1 to -1 is', name[1:-1])
print('characters start to end is', name[:])

print('Item ::1 is ',shoplist[::1])
print('Item ::2 is ',shoplist[::2])
print('Item ::3 is ',shoplist[::3])
print('Item ::-1 is ',shoplist[::-1])


# 集合是简单对象的无序集合，当集合中的项目存在与否比起次序或其出现次数更加重要时，我们就使用集合

