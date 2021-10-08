from datetime import datetime
from flask import current_app
from notificationEngine import db, login_manager
from sqlalchemy.dialects.mysql import JSON



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
    
    #you can create a privilage table to assign the rights to a admin
    isAdmin = db.Column(db.Boolean, nullable = False, default = False)  

    #relation
    notifications = db.relationship('User_Notif',  back_populates = "user")

    #meta data
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


    def __repr__(self):
        # return f"User('{self.name}', '{self.email}')"
        return f"User('{self.name}', '{self.email}', '{self.roles}')"

class Notification(db.Model):
    noti_id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(20), nullable = False)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    configuration = db.Column(JSON)
    isAdmin = db.Column(db.Boolean, nullable = False, default = False)
    role = db.Column(db.String(20), nullable = False, default = "NA")

    #relation
    users = db.relationship('User_Notif', back_populates = "notification")

    #meta data
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    createdBy = db.relationship(db.Integer, db.ForeignKey('user.user_id'), nullable = False)

    def __repr__(self):
        return f"Notification('{self.type}', '{self.content}', '{self.role}')"

class Trigger(db.Model):
    trigger_id = db.Column(db.Integer, primary_key = True)
    type = db.Column(db.String(20), nullable = False)
    configuration = db.Column(JSON)
    isAdmin = db.Column(db.Boolean, nullable=False, default=False)

    #relation
    # notification = db.relationship()

    #meta data
    create_time = db.Column(db.DateTime, nullable=False,default=datetime.utcnow)
    createdBy = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)


    def __repr__(self):
       return f"Trigger('{self.type}', '{self.content}', '{self.role}')"

