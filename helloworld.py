# -*- coding: utf-8 -*-
# @Time    : 2021/10/23 1:40 上午
# @Author  : FreanJa L
# @Email   : root@freanja.cn
# @File    : helloworld.py
# @Software: PyCharm

from flask import Flask
from flask import request
from flask import jsonify
from flask import render_template

app = Flask(__name__)

# 定义视图
@app.route('/')
def index():
    # return 'hello world'
    return render_template("index_try.html")

# @app.route('/', methods = ['POST'])
# def post_Code():
#     code = request.files['code']
#     recognize = {'code': }
if __name__ == '__main__':
    app.run()