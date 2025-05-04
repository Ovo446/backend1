from flask import Flask                       # 从 flask 库中导入 Flask 类（网站核心工具）

def create_app():                             # 定义一个函数叫 create_app，用来创建网站应用
    app = Flask(__name__)                     # 新建一个 Flask 应用对象，__name__ 是固定写法，标识当前模块

    app.config.from_object('config')          # 从 config.py 文件中读取设置（比如后面可能用数据库设置）

    from app.routes import api_bp                  # 从当前目录下的 routes.py 中导入叫 main 的蓝图（页面逻辑模块）
    app.register_blueprint(main)              # 把蓝图挂到主 app 上，让 app 知道有哪些网址接口

    return app                                # 返回这个 app 应用，让别人可以用它来启动网站
