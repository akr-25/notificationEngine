from flask import request, Blueprint
from flask_login import current_user, login_required

from notificationEngine import db
from notificationEngine.models import User, Trigger, User_Trigger

triggers = Blueprint('triggers', __name__)

strings = ['type', 'role']
arrays = ['selected_users', 'deselected_users']

def validateSchema(jsonData):
    for s in strings:
        if s in jsonData:
            if type(jsonData[s]) == str:
                continue
            else:
                return False
        else:
            False
    
    for a in arrays:
        if a in jsonData:
            if type(jsonData[a]) == type(["p4@g"]):
                continue
            else:
                return False
        else:
            return False

    return True

def Mapping(config, trig):
    role = config["role"]
    users = []
    if role != "NA":
        users = User.query.filter_by(role = role)
    
    type(config["selected_users"])
    for email in config["selected_users"]:
        user = User.query.filter_by(email = email).first()
        if user:
            users.append(user)
    
    for email in config["deselected_users"]:
        user = User.query.filter_by(email = email).first()
        if user:
            users.remove(user)
  
    for user in users:
        map = User_Trigger()
        map.user = user
        trig.users.append(map)
    
    if len(users) > 0:
        db.session.add(trig)
        db.session.commit()


@triggers.route("/admin/trigger/new", methods = ['POST'])
@login_required
def new_trigger():
    if current_user.isAdmin:
        data = request.json
        if validateSchema(data):
            type = data["type"]
            data.pop('type', None)

            trig = Trigger(type = type, configuration = data, createdBy = current_user, isAdmin = True)
            Mapping(data, trig)
            return {"message": "Success"}, 200
        return {"message": "Please provide type and configuration"}
    else: 
        return {"message": "Admin privilages required for this action"}, 403


# @triggers.route("/admin/trigger/get", methods=['GET'])
# @login_required
# def get_trigger():
#     if current_user.isAdmin:
#         data = request.json
