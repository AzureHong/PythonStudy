
# Pickle 持久地存储对象：可以将任何纯Python对象存储到一个文件中，并在稍后将其取回
# 如在机器学习中，存储模型数据

import pickle

# 存储相关对象的文件的名称
shoplistfile = 'shoplist.data'
# 购物清单
shoplist = ['apple','mango','carrot']

# 文件打开，准备写入
f = open(shoplistfile,'wb')
# 转存对象至文件
pickle.dump(shoplist,f)
f.close()

# 清除shoplist 变量
del shoplist

# 重新打开文件
f = open(shoplistfile,'rb')
# 从文件中载入对象
storedlist = pickle.load(f)
print(storedlist)
