# -*- coding: utf-8 -*-
# @Time    : 2021/10/23 8:53 下午
# @Author  : FreanJa L
# @Email   : root@freanja.cn
# @File    : study.py
# @Software: PyCharm
import json

from flask import Flask
from flask import request
from flask import Response
from flask import jsonify
from flask import render_template

app = Flask(__name__)
# Flask类将这个参数(__name__)作为程序名称。当然这个是可以自定义的，比如app = Flask("my-app")。
'''
    .
    ├── helloworld.py
    ├── static
    │   └── __init__.py
    ├── study.py
    ├── templates
    │   ├── __init__.py
    │   └── index_try.html
    └── venv
        ├── bin
        ├── include
        ├── lib
        └── pyvenv.cfg
    
    static目录存放静态资源，如图片、js、css文件等
    templates目录存放模版
    app = Flask("my-app", static_folder="path1", template_folder="path2")
    
'''


@app.route('/')
# app是一个Flask实例
# route中是客户端访问的路径地址，访问route指向的地址时，调用app下定义的方法，return是HTTP响应报文实体
def hello_world():
    return render_template("index_try.html")


# get获取参数   如请求 http://127.0.0.1:5000/get?user=lcx&key=123456
@app.route('/get')
def try_get():
    print(request.path)                             # /get
    print(request.full_path)                        # /get?user=lcx&key=123456
    # return request.args.__str__()                 # ImmutableMultiDict([('user', 'lcx'), ('key', '123456')])
    # return request.args.get('key')                # 123456
    # 因为flask不允许返回None，所以需要加默认值或者设置if判断
    # return request.args.get('key', 'admin')       # admin
    '''
    t = request.args.get('key')
    if t is None:
        return "None"
    else:
        return t
    '''
    # return str(request.args.getlist('k1'))
    return "Success!"
    # 127.0.0.1:5000/get?k1=123&k1=456&k1=789   ['123', '456', '789']


# post获取参数  如请求 http://127.0.0.1:5000/post
# {"user": ["lcx","lcx-"],"passwd": "admin123"}
@app.route('/post', methods=['POST', 'GET'])              # 仅接受post请求，也可以修改参数为 methods=['GET', 'POST'])
def try_post():
    print(request.headers)
    print(type(request.json))                       # <class 'dict'>
    print(request.json)                             # {'name': ['lcx', 'lcx-'], 'passwd': 'admin123'}
    # print(request.json['user'])                     # ['lcx', 'lcx-']
    # print(request.json['passwd'])                   # admin123
    '''
    Content-Type: application/json
    User-Agent: PostmanRuntime/7.28.4
    Accept: */*
    Postman-Token: 405924a8-eeb8-4ab4-b849-42fe1f33b7d4
    Host: 127.0.0.1:5000
    Accept-Encoding: gzip, deflate, br
    Connection: keep-alive
    Content-Length: 36
    '''
    # print(request.stream.read())                    # b'{"use": "lcx", "passwd": "admin123"}'

    # print(request.form)
    # print(request.form.get("user"))
    # print(request.form.get("passwd"))
    # result = {"result": request.json['num1'] + request.json['num2']}
    # return str(result)                            # 888
    # return jsonify(result)                          # { "result": 888 }
    return jsonify(request.json['code'])

# __name__ 在运行的是当前文件时，值为__main__
#          否则返回文件名
if __name__ == '__main__':
    # app.run(host='127.0.0.1', port=80, debug=True)        # 使用80端口后，需要用 sudo 运行
    app.run(debug=True)
    # print(Flask.__doc__)
