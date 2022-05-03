from . import api
from flask import jsonify, flash, request
import os
from werkzeug.utils import secure_filename
import pdfplumber
from app.models import Project, Manager, Member_info, Unit, Member2pro, TextInfo
from app import db
from ..utils import pure_format
from docx import Document

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

            ok = filename.endswith(".pdf")
            if ok is True:
                parse_table(filename)
            else:
                getDataFromTable(filename)

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
        print(data)
        manager = Manager()
        manager.name = data[1][1]
        manager.birthday = data[1][7]
        manager.system = data[4][3]
        manager.expertise = data[3][5]
        manager.tutor = data[3][3]
        manager.nationality = data[1][5]
        manager.unit = data[9][1]
        manager.position = data[3][1]
        manager.gender = data[1][3]
        db.session.add(manager)
        db.session.commit()

        unit = Unit()
        unit.name = data[9][1]
        unit.post = data[9][3]
        unit.location = data[11][3]
        unit.phone = data[11][1]
        db.session.add(unit)
        db.session.commit()

        textInfo = TextInfo()
        content = ""
        for i in range(2, 4):
            page = pdf.pages[i]
            page_content = '\n'.join(page.extract_text().split('\n')[:-1])
            content = content + page_content
            textInfo.argument = content
        cont = ""
        for i in range(4, len(pdf.pages)):
            page = pdf.pages[i]
            page_content = '\n'.join(page.extract_text().split('\n')[:-1])
            cont = cont + page_content
            textInfo.guarantee = cont
        db.session.add(textInfo)
        db.session.commit()

        project = Project()

        page01 = pdf.pages[0]  # 指定页码
        text = page01.extract_text()  # 提取文本
        lines = list(map(pure_format, list(text.split("\n"))))

        project.type = lines[2][-4:]
        project.summary = data[-2][0]
        project.name = data[0][1]
        project.manager_id = manager.id
        project.unit_id = unit.id
        project.text_id = textInfo.id
        db.session.add(project)
        db.session.commit()

        for i in range(13, 17):
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



def getDataFromTable(path):
    path = os.path.join(UPLOAD_FOLDER, path)
    document = Document(path)
    # 获取文档中的所有表格
    all_tables = document.tables

    cell_list = []
    for table in all_tables:
        for row in table.rows:
            cell_lists = []
            cell_lists.clear()
            text = ''
            for cell in row.cells:
                # print("1", cell)
                tempt = text
                text = cell.text.replace('\n', '').replace(' ', '')
                if tempt == text:
                    continue
                cell_lists.append(text)
            # print("1", cell_lists)
            cell_list.append(cell_lists)
    # print(len(cell_list[20]))
    manager = Manager()
    manager.name = cell_list[7][1]
    manager.birthday = cell_list[7][7]
    manager.system = cell_list[11][3]
    manager.expertise = cell_list[9][5]
    manager.tutor = cell_list[10][3]
    manager.nationality = cell_list[7][5]
    manager.unit = cell_list[15][1]
    manager.position = cell_list[9][1]
    manager.gender = cell_list[7][3]
    db.session.add(manager)
    db.session.commit()

    unit = Unit()
    unit.name = cell_list[15][1]
    unit.post = cell_list[15][3]
    unit.location = cell_list[17][3]
    unit.phone = cell_list[17][1]
    db.session.add(unit)
    db.session.commit()

    textInfo = TextInfo()
    textInfo.argument = cell_list[-2][0]
    textInfo.guarantee = cell_list[-1][0]
    db.session.add(textInfo)
    db.session.commit()

    project = Project()
    project.type = cell_list[1][1]
    project.summary = cell_list[22][0]
    project.name = cell_list[2][1]
    project.manager_id = manager.id
    project.unit_id = unit.id
    project.text_id = textInfo.id
    db.session.add(project)
    db.session.commit()

    for i in range(19, 25):
        if len(cell_list[i]) < 3:
            break
        member = Member_info()
        member.name = cell_list[i][1]
        member.gender = cell_list[i][2]
        member.birthday = cell_list[i][3]

        db.session.add(member)
        db.session.commit()

        member2pro = Member2pro()
        member2pro.mid = member.id
        member2pro.pid = project.id
        db.session.add(member2pro)
        db.session.commit()

            # getDataFromTable(r"../static/1.docx")


def rePlace(url):
    url = url.replace("/", "\\")
    return url
