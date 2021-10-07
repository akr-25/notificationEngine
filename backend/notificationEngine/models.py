from datetime import datetime
from flask import current_app
from notificationEngine import db, login_manager
# from flask_login import UserMixin
from sqlalchemy.dialects.mysql import JSON


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# subs = db.Table('subs',
#     db.Column('user_id', db.Integer, db.ForeignKey('user.user_id'), nullable = False),
#     db.Column('noti_id', db.Integer, db.ForeignKey(
#         'notification.noti_id'),  nullable=False),
#     db.Column('user_config', JSON)
# )

class User_Notif(db.Model):
    __tablename__ = 'mapping'
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), primary_key=True)
    noti_id = db.Column(db.Integer, db.ForeignKey('notification.noti_id'), primary_key=True)

    user_config = db.Column(JSON)
    user_response = db.Column(JSON)

    user = db.relationship('User', back_populates = "notifications")
    notification = db.relationship('Notification', back_populates = "users")

    def __repr__(self):
        return f"Map('{self.user_id}', '{self.noti_id}')"

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    history = db.Column(JSON)
    roles = db.Column(db.String(20))

    #relations
    notifications = db.relationship('User_Notif',  back_populates = "user")

    #meta data
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


    def __repr__(self):
        return f"User('{self.name}', '{self.email}')"
        # return f"User('{self.name}', '{self.email}', '{self.roles}')"

class Notification(db.Model):
    noti_id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(20), nullable = False)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    configuration = db.Column(JSON)
    isAdmin = db.Column(db.Boolean, nullable = False, default = False)
    role = db.Column(db.String(20), nullable = False, default = "NA")

    #relations
    users = db.relationship('User_Notif', back_populates = "notification")

    #meta data
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    # createdBy = db.relationship(db.Integer, db.ForeignKey('user.user_id'))

    def __repr__(self):
        return f"Notification('{self.type}', '{self.content}', '{self.role}')"

# class Trigger(db.Model):
#     trigger_id = db.Column(db.Integer, primary_key = True)
#     type = db.Column(db.String(20), nullable = False)
#     # createdBy = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     create_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#     configuration = db.Column(JSON)
#     isAdmin = db.Column(db.Boolean, nullable=False, default=False)

#     # notification = db.relationship()

#     def __repr__(self):
#        return f"Trigger('{self.type}', '{self.content}', '{self.role}')"

# class Admin(db.Model, UserMixin):
#     admin_id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(30), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     password = db.Column(db.String(60), nullable=False)
#     # notification = db.relationship()

#     def __repr__(self):
#         return f"User('{self.name}', '{self.email}', '{self.roles}')"




#     def __repr__(self):
#         return f"Post('{self.title}', '{self.date_posted}')"

# class Role(db.Model):
#     role_id = db.Column(db.Integer, primary_key = True)
#     name = db.Column(db.String(30), nullable = False)
#     # members = db.relationship()



