# app/__init__.py
from flask import Flask
from app.routes import api_bp  # 从 routes.py 里导入蓝图

def create_app():
    app = Flask(__name__)
    app.register_blueprint(api_bp)  # 注册蓝图
    return app
