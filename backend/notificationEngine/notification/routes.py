from flask import request, Blueprint
from flask_login import current_user, login_required

from notificationEngine import db
from notificationEngine.models import User, Trigger, Notification, User_Trigger

notification = Blueprint('notification', __name__)

strings = ['type', 'title', 'content']
integers = ['trigger_id']
arrays = []


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

    for i in integers:
        if i in jsonData:
            if type(jsonData[i]) == type(1):
                continue
            else:
                return False
        else:
            return False

    return True


@notification.route("/admin/notification/new", methods=['POST'])
@login_required
def new_notification():
    if current_user.isAdmin:
        data = request.json
        if validateSchema(data):
            type = data["type"]
            title = data["title"]
            content = data["content"]
            trigger_id = data["trigger_id"]
            data.pop('type', None)
            data.pop('title', None)
            data.pop('content', None)
            data.pop('trigger_id', None)
            trig = Trigger.query.get(trigger_id)
            if not trig:
                return {"message": "Trigger ID not valid"}
            
            noti = Notification(type=type, title=title, content=content, configuration=data,
                                createdBy=current_user, isAdmin=True)
            
            noti.trigger = trig.trigger_id
            db.session.add(noti)
            db.session.commit()

            return {"message": "Success"}, 200
        return {"message": "Please provide type and configuration"}
    else:
        return {"message": "Admin privilages required for this action"}, 403


# @notification.route("/admin/notification/get", methods=['GET'])
# @login_required
# def get_notification():
#     if current_user.isAdmin:
#         data = request.json
