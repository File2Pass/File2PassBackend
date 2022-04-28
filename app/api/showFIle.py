# 这个文件主要完成的是对数据库中存储的申报书的内容进行提取
from . import api
from .. import db
from ..models import Project, Manager, Unit, Member_info, Member2pro
from flask import jsonify


# 这个主要是通过通过前端发送过来的申报书id对数据库内的信息进行展示
@api.route("/file/review")
def show_allProject():
    # print(1)
    # sql = 'select id, name from project'
    pro = Project.query.all()
    if pro is None:
        return jsonify({
            "msg": "加载失败"
        }), 400
    res = {
        "list": [{
            "id": i.id,
            "type": i.type,
            "summary": i.summary,
            "name": i.name
        }for i in pro]
    }
    return jsonify(res), 200


# 这个主要是对项目基本信息进行呈现
@api.route("/file/review/<int:id>/project")
def show_project(id):
    res = Project.query.filter(Project.id == id)
    if res is None:
        return jsonify({
            "msg": "查询基本信息失败"
        }), 400
    result = {
        "list": [{
            "id": i.id,
            "type": i.type,
            "summary": i.summary,
            "name": i.name
        } for i in res]
    }
    return jsonify(result), 200


# 这个主要是对项目基本信息中的申报人信息进行呈现
@api.route("/file/review/<int:id>/manager")
def show_manager(id):
    re = Project.query.filter(Project.id == id)
    uid = re[0].manager_id
    print("id:", uid)
    manage_res = Manager.query.filter(Manager.id == int(uid)).first()
    if manage_res is None:
        return jsonify({
            "msg": "获取失败"
        }), 400
    # if manage_res.sex == 1:
    #     se = "女"
    # else:
    #     se = "男"
    res = {
        "id": manage_res.id,
        "name": manage_res.name,
        "unit": manage_res.unit,
        "position": manage_res.position,
        "sex":  manage_res.gender,
        "nationality": manage_res.nationality,
        "birthday": manage_res.birthday,
        "expertise": manage_res.expertise,
        "tutor": manage_res.tutor,
        "system": manage_res.system
    }
    return jsonify(res), 200


# 这个主要是对本项目的申报人的依托单位的信息进行展示
@api.route("/file/review/<int:id>/unit")
def show_unit(id):
    re = Project.query.filter(Project.id == id).first()
    if re is None:
        return jsonify({
            "msg": "查询数据库失败"
        }), 400
    uid = re.unit_id
    unit_res = Unit.query.filter(Unit.id == uid).first()
    if unit_res is None:
        return jsonify({
            "msg": "查询依托单位的表失败"
        }), 400
    res = {
        "id": unit_res.id,
        "name": unit_res.name,
        "phone": unit_res.phone,
        "post": unit_res.post,
        "location": unit_res.location
    }
    return jsonify(res), 200


# 这个主要是对项目一些预期信息进行展示的接口
# @api.route("/file/review/<int:id>/performance")
# def show_performance(id):
#     re = Project.query.filter(Project.id == id).first()
#     if re is None:
#         return jsonify({
#             "msg": "查询项目信息失败"
#         }), 400
#     eid = re.expected_performance_id
#     res = Expected_Performance.query.filter(Expected_Performance.id == eid).first()
#     if res is None:
#         return jsonify({
#             "msg": "查询项目预期信息失败"
#         }), 400
#     result = {
#         "id": res.id,
#         "content": res.content,
#         "expense": res.expenses,
#         "deadline": res.deadline
#     }
#     return jsonify(result), 200


@api.route("/file/review/<int:id>/member")
def show_member(id):
    id_list = Member2pro.query.filter(Member2pro.pid == id)
    if id_list is None:
        return jsonify({
            "msg": "查询依托单位的表失败"
        }), 400
    info = []
    for m in id_list:
        minfo = Member_info.query.filter(Member_info.id == m.mid).first()
        info.append(minfo)
    result = {
        "list": [{
            "id": i.id,
            "name": i.name,
            "gender": i.gender,
            "birthday": i.birthday
        } for i in info]
    }
    return jsonify(result), 200
