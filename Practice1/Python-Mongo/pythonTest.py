# -*- coding: utf-8 -*-
from pymongoConn import MongoConn

if __name__ == '__main__':
    my_conn = MongoConn()
    datas = [
        {'id':1,'data':12},
        {'id':2,'data':22},
        {'id':3,'data':'CC'},
        {'id':4,'data':'DD'}
    ]

my_conn.db['TestMM'].insert(datas)

res = my_conn.db['TestMM'].find({})
for k in res:
    print(k)