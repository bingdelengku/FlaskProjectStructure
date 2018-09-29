#-*-coding:utf-8 -*-
import os
from app import create_app, db
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)

def make_shell_context():
    return dict(app=app, db=db)

manager.add_command("shell",Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()




# 启动参数
#
# -?，--help	# 查看帮助信息
# --threaded	# 开启多线程
# -d	# 开启调试模式
# -r	# 自动加载
# -h，--host	# 指定主机
# -p，--port	# 指定端口

# python manage.py runserver -d -r -p 8000 -h 0.0.0.0