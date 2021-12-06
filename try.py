# -*- coding: utf-8 -*-
# @Time    : 2021/10/24 4:32 上午
# @Author  : FreanJa L
# @Email   : root@freanja.cn
# @File    : try.py
# @Software: PyCharm
import json

from flask import Flask
from flask import request
from flask import render_template
from flask import Response
from flask import jsonify
import compiler
import setCode

app = Flask(__name__)


def Response_headers(content):
    print(content)
    resp = Response(content)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


@app.route('/')
def index():
    print("run")
    return render_template("index.html")


@app.route('/server', methods=['POST', 'GET'])
def server():
    if request.method == 'POST':
        print('success')
        if request.is_json:
            print("is json")
            # print(request.json)
        print(request.get_data(as_text=True))
        # print("...")
        # print(request.data)
        # data = request.get_data(as_text=True)
        # print(data)
        # print(request.get_json(force=True))

        data = json.loads(request.get_data(as_text=True))

        for key, value in data:
            print(key, value)

        code = request.json['user']
        print(code)
        # result = compiler.main(code)['output']
        # print(result['output'])
        # print(result["output"])
        return jsonify(code)
        # print(Response_headers(str(result)))
        # return Response_headers(str(result))
    else:
        return "Success!"


@app.route('/process', methods=['POST'])
def process():
    # print(request.form)
    data = dict(request.form)

    for key in data:
        # print(key)
        inner_data = json.loads(key)
        # print(inner_data)
        # print(type(inner_data))
        # print(len(inner_data))

    code = setCode.set_code(inner_data)
    result = compiler.main(code)['output']
    print(result)
    return jsonify({'output': result})




        # print(value)
    # print(data.keys()[0])
    # print(re)
    # source_code = setCode.set_code(request.form)
    # result = compiler.main(source_code)['output']
    # print(result)

    # user = request.form['user']
    # pwd = request.form['pwd']
    # output = user + pwd
    # if user and pwd:
    #     return jsonify({'output': 'login info:' + output})
    # return jsonify({'error' : 'Missing data!'})
    # print(request.get_data(as_text=True))
    # return jsonify({'input': 'request.get_data()'})

# def test_post():
#     testInfo['name'] = 'xiaoming'
#     testInfo['age'] = '28'
#     return json.dumps(testInfo)


if __name__ == "__main__":
    app.run(debug=True)


