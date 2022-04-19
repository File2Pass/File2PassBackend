# 这个文件主要完成的是对数据库中存储的申报书的内容进行提取
from . import api

# 这个主要是通过通过前端发送过来的申报书id对数据库内的信息进行展示
@api.route("/file/manager", methods=["Get"])
def show_manager():
    pass



# 这个主要是对项目基本信息进行呈现
# @api.route()