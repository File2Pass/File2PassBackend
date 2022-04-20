# 这个文件主要完成的是对数据库中存储的申报书的内容进行提取
from . import api
from .. import db
from ..models import Project, Manager


# 这个主要是通过通过前端发送过来的申报书id对数据库内的信息进行展示
@api.route("/file/review")
def show_allProject():
    # print(1)
    # sql = 'select id, name from project'
    pro = Project.query.all()
    return str(pro[0].id)


# 这个主要是对项目基本信息进行呈现
@api.route("/file/review/<int:id>/project")
def show_project(id):
    res = Project.query.filter(Project.id == id)
    return str(res[0].id)


# 这个主要是对项目基本信息中的申报人信息进行呈现
@api.route("/file/review/<int:id>/manager")
def show_manager(id):
    res = Project.query.filter(Project.id == id)
    uid = res[0].manager_id
    print("id:", uid)
    manage_res = Manager.query.filter(Manager.id == int(uid)).first()
    return str(manage_res.name)