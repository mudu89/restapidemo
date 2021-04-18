from flask import Blueprint, make_response, jsonify, request
from restapi.models import User
from restapi.utils import UserUtils
from base64 import b64encode

adduser = Blueprint('adduser',__name__)


@adduser.route("/create", methods=['POST'])
def create():
    #verify JWT
    if not all(arg in list(request.args.keys()) for arg in ["username","email","password"]):
        response = make_response(jsonify({"status":"Error"}), 400)
    else:
        #Verify the JWT/session sent in the headers, if verified proceed
        password_encode = b64encode(bytes(request.args['password'],'utf-8'))
        user = User(username=request.args['username'], email=request.args['email'], password=password_encode)
        if UserUtils.check_user(user):
            result = {"status":"user already exists"}
            code = 404
        else:
            UserUtils.insert_user(user)
            result = {"status":"user created"}
            code=200
        response = make_response(jsonify(result), code)
    return response
