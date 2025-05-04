# app/routes.py
from flask import Blueprint, jsonify
from ted_scraper import get_ted_talks  # 导入 TED 爬虫函数

api_bp = Blueprint('api', __name__)

@api_bp.route("/")
def home():
    return "欢迎访问网站后台 API！"

@api_bp.route("/ted")
def ted_route():
    data = get_ted_talks()
    return jsonify(data)
