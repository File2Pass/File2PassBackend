from . import api
from flask import jsonify, current_app, url_for, flash, request, redirect
import os
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {'doc', 'docx'}
UPLOAD_FOLDER = '../static'

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
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            return jsonify({
               'msg': "上传文件成功"
            }), 200
