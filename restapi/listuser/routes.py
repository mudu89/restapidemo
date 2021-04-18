
from flask import Blueprint, make_response, jsonify, request
from restapi.models import User


listusers = Blueprint('listusers',__name__)

@listusers.route("/list", methods=['GET'])
def getusers():
    #user the JWT/session sent from login to authenticate the user is logged in first
    #Else we can use the httpautth methods for basic authentication
    users = User.query.all()
    response_dict=[]
    for user in users:
        tempdict={}
        tempdict['username']=user.username
        tempdict['email']=user.email
        tempdict['lastlogin']=user.lastlogin
        response_dict.append(tempdict)
    response = make_response({"Result":response_dict}, 200)
    return response