from . import api
from flask import jsonify, flash, request
import os
from werkzeug.utils import secure_filename
import pdfplumber
from app.models import Project, Manager, Member_info, Unit, Member2pro
from app import db
from ..utils import pure_format

ALLOWED_EXTENSIONS = {'doc', 'docx', 'pdf'}
UPLOAD_FOLDER = 'C:/Users/hp/File2PassBackend/app/static'


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@api.route("/file/upload", methods=["POST"], endpoint="UploadFile")
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return jsonify({
                'msg': "文件上传失败，不存在文件part"
            }), 404

        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return jsonify({
                'msg': "上传文件失败，文件为空"
            }), 404

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(rePlace(os.path.join(UPLOAD_FOLDER, filename)))

            parse_table(filename)

            return jsonify({
                'msg': "上传文件成功"
            }), 200


def parse_table(filename):
    with pdfplumber.open(os.path.join(UPLOAD_FOLDER, filename)) as pdf:
        page = pdf.pages[1]
        data = []
        for rows in page.extract_tables():
            for row in rows:
                row = list(filter(None, row))
                row = list(map(pure_format, row))
                data.append(row)

        manager = Manager()
        manager.name = data[1][1]
        manager.birthday = data[1][7]
        manager.system = data[4][3]
        manager.expertise = data[2][5]
        manager.tutor = data[3][3]
        manager.nationality = data[1][5]
        manager.unit = data[8][1]
        manager.position = data[2][1]
        manager.gender = data[1][3]
        db.session.add(manager)
        db.session.commit()

        unit = Unit()
        unit.name = data[8][1]
        unit.post = data[8][3]
        unit.location = data[10][3]
        unit.phone = data[10][1]
        db.session.add(unit)
        db.session.commit()

        project = Project()

        page01 = pdf.pages[0]  # 指定页码
        text = page01.extract_text()  # 提取文本
        lines = list(map(pure_format, list(text.split("\n"))))

        project.type = lines[2][-4:]
        project.summary = data[18][0]
        project.name = data[0][1]
        project.manager_id = manager.id
        project.unit_id = unit.id
        db.session.add(project)
        db.session.commit()

        for i in range(12, 17):
            if len(data[i]) < 2:
                break
            member = Member_info()
            member.name = data[i][0]
            member.gender = data[i][1]
            member.birthday = data[i][2]

            db.session.add(member)
            db.session.commit()

            member2pro = Member2pro()
            member2pro.mid = member.id
            member2pro.pid = project.id
            db.session.add(member2pro)
            db.session.commit()

def rePlace(url):
    url = url.replace("/", "\\")
    return url
