# 甚是优美的功能：文档字符串
def print_max(x,y):
    '''打印这两个数值中的最大数。

    这两个数都应该是整数'''
    # 如果可能，将其转换值整数类型
    x = int(x)
    y = int(y)

    if x>y :
        print(x,'is maxmum')
    else:
        print(y,'is maxmum')

print_max(3, 5)
print(print_max.__doc__)
