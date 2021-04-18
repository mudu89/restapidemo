from flask import Blueprint, make_response, jsonify
from restapi.models import User
from restapi.utils import UserUtils
Delete = Blueprint('Delete',__name__)

@Delete.route("/delete/username/<string:username>", methods=['DELETE'])
def deleteuser(username):
    # user the JWT/session sent from login to authenticate the user is logged in first
    # Else we can use the httpautth methods for basic authentication
    user = User.query.filter_by(username=username).first()
    if user is not None:
        UserUtils.delete_user(user)
        response = make_response(jsonify({"status": "Success"}), 200)
    else:
        response = make_response(jsonify({"status": "User not found"}), 404)
    return response

#Can add more routes to delete using email or id etc...