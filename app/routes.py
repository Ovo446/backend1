from flask import Blueprint, jsonify          # 导入蓝图工具和 jsonify（返回 JSON 用）
from ted_scraper import get_ted_talks        # 从本地导入 TED 爬虫函数

main = Blueprint('main', __name__)            # 创建一个蓝图对象，名字叫 main

@main.route('/')                              # 访问根路径时执行这个函数
def index():
    return jsonify({'message': 'Still learning backend working!'})  # 返回 JSON 消息

@main.route('/ted')                           # 访问 /ted 路径时执行这个函数
def ted():
    return jsonify(get_ted_talks())           # 返回爬 TED 的结果（字典）
