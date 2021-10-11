from flask import request, Blueprint
from notificationEngine import db, bcrypt
from notificationEngine.models import User
from flask_login import login_user, current_user, logout_user


auth = Blueprint('auth', __name__)


@auth.route("/auth/register", methods = ['POST'])
def register():
    if current_user.is_authenticated:
        return {"message": "User already logged in"}, 403
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


@auth.route("/auth/login", methods = ["GET"])
def login():
    if current_user.is_authenticated:
        return {"message": "User already logged in"}, 403
    data = request.json
    if "email" in data and "password" in data:
        user = User.query.filter_by(email = data["email"]).first()
        if user and bcrypt.check_password_hash(user.password, data["password"]):
            login_user(user)
            return user.info(), 200
        else:
            return  {"message": "Password doesn't match or user doesn't exist"}, 403
    else:
        return {"message": "Please provide email and password"}, 403


@auth.route("/auth/logout", methods = ['POST'])
def logout():
    logout_user()
    return {"message": "Logout Successful"}, 200