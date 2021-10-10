from datetime import datetime
from flask import current_app
from notificationEngine import db, login_manager
from flask_login import UserMixin

from sqlalchemy.dialects.mysql import JSON
from sqlalchemy import Column, Integer, ForeignKey, String, Boolean, Text
from sqlalchemy.orm import relationship


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User_Trigger(db.Model):


    __tablename__ = 'mapping'
    user_id = Column(Integer, ForeignKey('user.user_id'), primary_key=True)
    trigger_id = Column(Integer, ForeignKey('trigger.trigger_id'), primary_key=True)


    user_config = Column(JSON)
    user_response = Column(JSON)


    user = relationship('User', back_populates = "triggers", lazy=True)
    trigger = relationship('Trigger', back_populates="users", lazy=True)


    def __repr__(self):
        return f"Map('{self.user_id}', '{self.trigger_id}')"

class User(db.Model, UserMixin):


    user_id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(60), nullable=False)
    history = Column(JSON)
    role = Column(String(20))
    
    #you can create a privilage table to assign the rights to a admin
    isAdmin = Column(Boolean, nullable = False, default = False)  

    #relation
    triggers = relationship('User_Trigger',  back_populates = "user", lazy=True)

    #meta data
    create_time = Column(db.DateTime, nullable=False, default=datetime.utcnow)
    trigger_created = relationship('Trigger', backref='createdBy', lazy=True)
    notification_created = relationship('Notification', backref='createdBy', lazy = True)

    def info(self):
        return {
            "user_id":self.user_id,
            "name": self.name, 
            "email": self.email, 
            "role": self.role, 
            "isAdmin": self.isAdmin
        }
        
    def get_id(self):
        return self.user_id

    def __repr__(self):
        # return f"User('{self.name}', '{self.email}')"
        return f"User('{self.name}', '{self.email}', '{self.role}', {self.isAdmin})"

class Notification(db.Model):

    noti_id = Column(Integer, primary_key=True)
    type = Column(String(20), nullable = False)
    title = Column(String(100), nullable=False)
    content = Column(Text, nullable=False)
    configuration = Column(JSON)
    isAdmin = Column(Boolean, nullable = False, default = False)
    # role = Column(String(20), nullable = False, default = "NA")

    #relation
    triggers = relationship('Trigger', backref='noti', lazy = True)

    #meta data
    create_time = Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey('user.user_id'), nullable=False)


    def __repr__(self):
        return f"Notification('{self.type}', '{self.content}', '{self.triggers}')"

class Trigger(db.Model):

    trigger_id = Column(Integer, primary_key = True)
    type = Column(String(20), nullable = False)
    configuration = Column(JSON, nullable= False)
    isAdmin = Column(Boolean, nullable=False, default=False)

    #relation
    notification = Column(Integer, ForeignKey('notification.noti_id'))
    users = relationship('User_Trigger', back_populates="trigger", lazy=True)

    #meta data
    create_time = Column(db.DateTime, nullable=False,default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey('user.user_id'), nullable=False)



    def __repr__(self):
       return f"""Trigger('{self.type}', '{self.createdBy}', '{self.configuration["role"]}', '{self.configuration["selected_users"]}')"""

