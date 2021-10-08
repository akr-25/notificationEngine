from flask import request, Blueprint
from notificationEngine import db, bcrypt
from notificationEngine.models import User, Notification, Trigger, User_Trigger
from json import dumps as jsonstring


users = Blueprint('users', __name__)


@users.route("/user/register", methods = ['POST'])
def register():
    data = request.json
    if "name" in data and "email" in data and "password" in data:
        hashed_password = bcrypt.generate_password_hash(data["password"]).decode('utf-8')
        user = User(name = data["name"], email = data["email"], password = hashed_password)

        if "role" in data:
            user.role = data["role"]
        if "isAdmin" in data:
            user.isAdmin = data["isAdmin"]
        print(user)
        db.session.add(user)
        db.session.commit()
        return user.info(), 200
    else:
        return {"message": "Please provide name, email and password"}, 403


@users.route("/user/login", methods = ["GET"])
def login():
    data = request.json
    if "email" in data and "password" in data:
        user = User.query.filter_by(email = data["email"]).first()
        if user and bcrypt.check_password_hash(user.password, data["password"]):
            return user.info(), 200
        else:
            return  {"message": "Password doesn't match or user doesn't exist"}, 403
    else:
        return {"message": "Please provide email and password"}, 403
