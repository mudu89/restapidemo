from flask import Blueprint, make_response, jsonify, request
from restapi.models import User
from restapi.utils import UserUtils
from base64 import b64decode

login_user = Blueprint('login_user',__name__)



@login_user.route("/login")
def login():
    if not all(arg in list(request.args.keys()) for arg in ["email","password"]):
        response = make_response(jsonify({"status":"Error"}), 400)
    else:
        user = User.query.filter_by(email=request.args["email"]).first()
        if user:
            decode_password = b64decode(user.password).decode('utf-8')
            if decode_password == request.args['password']:
                user.lastlogin = datetime.datetime.utcnow()
                UserUtils.insert_user(user)
                #can send a JWT or some session token to remember the login
                response = make_response(jsonify({"status": "Success"}), 200)
            else:
                response = make_response(jsonify({"status": "Incorrect Password"}), 404)
        else:
            response = make_response(jsonify({"status": "Error"}), 400)
    return response

