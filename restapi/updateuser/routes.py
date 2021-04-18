from flask import Blueprint, make_response, jsonify, request
from restapi.models import User
from restapi.utils import UserUtils


updateusers = Blueprint('updateusers',__name__)

@updateusers.route("/update/username/<string:username>", methods=['PUT'])
def updateuser(username):
    # user the JWT/session sent from login to authenticate the user is logged in first
    # Else we can use the httpautth methods for basic authentication
    if not all(arg in list(request.args.keys()) for arg in ["email"]):
        response = make_response(jsonify({"status": "Error"}), 400)
    else:
        user = User.query.filter_by(username=username).first()
        if user is not None:
            user.email = request.args['email']
            UserUtils.insert_user(user)
            response = make_response(jsonify({"status": "Success"}), 200)
        else:
            response = make_response(jsonify({"status": "User not found"}), 404)
    return response
