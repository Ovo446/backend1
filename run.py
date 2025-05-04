from app import create_app                    # 从 app 包中导入创建应用的函数

app = create_app()                            # 调用函数，创建 app 对象

if __name__ == '__main__':                    # 如果直接运行这个文件
    app.run()                                 # 启动 Flask 应用（默认本地调试模式）
