# 异常处理
try:
    text = input('Enter something -->')
except EOFError:
    print('why did you do an EOF on me?')
except KeyboardInterrupt:
    print('You cancelled the operation.')
# else 在没有发生异常时候执行
else:
    print('You entered {}'.format(text))