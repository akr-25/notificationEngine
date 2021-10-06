from datetime import datetime
from flask import current_app
from notificationEngine import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    history = db.Column(db.Text)
    # roles = db.relationship()
    # notification = db.relationship()


    def __repr__(self):
        return f"User('{self.name}', '{self.email}', '{self.roles}')"


class Admin(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    # notification = db.relationship()

    def __repr__(self):
        return f"User('{self.name}', '{self.email}', '{self.roles}')"


class Notification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    createdBy = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    configuration = db.Column(db.Text)
    isAdmin = db.Column(db.Boolean, nullable = False, default = False)
    role = db.Column(db.String(20), nullable = False, default = "NA")

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

class Role(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    # members = db.relationship()

class Trigger(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    type = db.Column(db.String(20), nullable = False)
    createdBy = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False,
                             default=datetime.utcnow)
    configuration = db.Column(db.Text)
    responses = db.Column(db.Text)
    isAdmin = db.Column(db.Boolean, nullable=False, default=False)
    # notification = db.relationship()

