from flask import request, Blueprint
from notificationEngine.models import Notification, Trigger
from notificationEngine import db, bcrypt
from notificationEngine.models import User
from flask_login import login_user, current_user, logout_user
import json


user = Blueprint('user', __name__)


@user.route("/user/notification", methods=['GET'])
def fetch_notification():
    if current_user.is_authenticated:
        data = request.json
        if "email" in data:
            user = User.query.filter_by(email = data["email"]).first()
            if user == current_user:
                notifications = []
                for trigger in user.triggers:
                    trig = Trigger.query.get(trigger.trigger_id)
                    notifications.append(trig.noti.json())
                return json.dumps(notifications)
            else:
                return {"message": "You can only see your notifications"}, 403
        else:
            return {"message": "Please provide valid email id"}, 403
    else:
        return {"message": "You are not logged in!"}, 403
