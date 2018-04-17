poem = '''\
Programming is fun 
when the work is done 
if you wanna make your work also fun:
        use Python!
'''

# r 阅读模式，w 写入模式，a 追加模式，t 文本模式，b 二进制模式
f = open('poem.txt','w')
f.write(poem)
f.close()

f = open('poem.txt')
while True:
    line = f.readline()
    if len(line) == 0:
        break
    print(line,end = '')
f.close()