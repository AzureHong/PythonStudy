from flask import Flask,url_for
app = Flask(__name__)

'''
@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0')  # 会让操作系统监听所有的公网IP

@app.route('/')
def index():
    pass

@app.route('/login')
def login():
    pass

@app.route('/user/<username>')
def profile(username):
    pass

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login',next='/'))
    print(url_for('profile',username='John Doe'))
'''
'''
# HTTP方法示例
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST'
        do_the_login()
    else：
        show_the_login_form()
'''

'''
# 一、关于调试模式的相关知识
# 调试模式
    app.debug = True
    app.run()
# 或者
    app.run(debug=True)

1. debug ：是否开启调试模式并捕获异常
2. use_debugger ： 是否使用内部的Flask调试器
3. use_reloader ： 是否在异常时重新载入并创建子进程

config.yaml 配置


# 二、关于路由的相关知识
    1. 常规 @app.route('/hello')
    2. 构造含有动态部分的URL，也可以在一个函数上附着多个规则
        1) @app.route('/hello/<username>') 将username作为命名参数传递到函数中
        2) @app.route('/hell/<int:age>') 转换器指定<int:age>,即命名参数age使用int转换器，表示接受整数
        3) 转换器类型：int接受整数；float接受浮点数；path和默认的相似，但也接受斜线
    3. 唯一URL/重定向行为：
        @app.route('/projects/')访问一个结尾不带斜线的URL会被Flask重定向到带斜线的规范URL去
    4. 构造URL
        url_for()：可以用来给指定的函数构造URL，它接受函数名作为第一个参数，也接受对应URL规则的变量部分的命名参数。位置变量部分会添加到URL末尾作为查询参数

# 三、文件上传：上传的文件信息会默认被保存在字典内容中

# 四、Cookies：请求对象的cookies属性是一个内容为客户端提交的所有Cookies的字典

# 五、重定向和错误
    redirect() 函数把用户重定向到其它地方
    abort() 放弃请求并返回错误代码

    默认情况下，错误代码会显示一个黑白的错误页面，如果你要定制错误页面，可以使用errorhandler()装饰器

from flask import render_template

@app.errorhandler(404)
def page_not_found(error):
    return render_template('Page_not_found.html'),404

# 六、消息闪现
    反馈是良好的应用和用户界面的重要构成。Flask提供了消息闪现系统，可以简单地给用户反馈
    消息闪现系统通常会在请求结束时记录信息，并在下一个（且仅在下一个）请求中范文记录的信息。
    展现这些消息，通常需要结合模板布局
    


'''

