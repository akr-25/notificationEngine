from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_manager
from notificationEngine.config import Config


# db = SQLAlchemy()
# bcrypt = Bcrypt()
# login_manager = LoginManager()


# def create_app(config_class=Config):
#     app = Flask(__name__)
#     app.config.from_object(Config)

#     db.init_app(app)
#     bcrypt.init_app(app)
#     login_manager.init_app(app)

    # from notificationEngine.users.routes import users
    # from notificationEngine.role.routes import role
    # from notificationEngine.admin.routes import admin
    # from notificationEngine.trigger.routes import trigger
    # from notificationEngine.notification.routes import notification

    # app.register_blueprint(users)
    # app.register_blueprint(role)
    # app.register_blueprint(admin)
    # app.register_blueprint(trigger)
    # app.register_blueprint(notification)

    # return app

app = Flask(__name__)
# app.config.from_object(Config)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:password@localhost:3306/buildathon"
db = SQLAlchemy(app)
login_manager = LoginManager(app)
