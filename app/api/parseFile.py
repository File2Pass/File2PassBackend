from . import api
from flask import jsonify, request, current_app, url_for


@api.route("/file/parseFile", methods=["POST"], endpoint="ParseFile")
def parse_file():
    pass
