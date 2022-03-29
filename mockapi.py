#encoding:utf-8
from flask import Flask, request, jsonify

api = Flask(__name__)


@api.route('/')
def hello():
    return "Hello, World！"


@api.route('/mockapi/', methods=['GET'])
def mockapi():
    a, b = request.args.get('a', ''), request.args.get('b', '')
    if b is None:
        response = {'err_code': 21, 'err_msg': 'empty or wrong params', 'refenence': '必传字段b未传值'}
        return jsonify(response)
    if b and not isinstance(b, str):
        response = {'err_code': 21, 'err_msg': 'empty or wrong params', 'refenence': 'b传参有误'}
        return jsonify(response)
    if a and not isinstance(a, int):
        response = {'err_code': 21, 'err_msg': 'empty or wrong params', 'refenence': 'a传参有误'}
        return jsonify(response)
    if len(b) < 10:
        response = {'err_code': 0, 'err_msg': 'success', 'refenence': '访问成功'}
        return jsonify(response)
    else:
        response = {'err_code': 11, 'err_msg': 'system error', 'refenence': '系统错误'}
        return jsonify(response)


if __name__ == "__main__":
    api.config['JSON_AS_ASCII'] = False
    api.run(host="0.0.0.0", port=8080)