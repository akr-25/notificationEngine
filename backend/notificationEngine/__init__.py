from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from notificationEngine.config import Config


app = Flask(__name__)
app.config.from_object(Config)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:password@localhost:3306/buildathon"
db = SQLAlchemy(app, session_options={"autoflush": False})
login_manager = LoginManager(app)
bcrypt = Bcrypt(app)

from notificationEngine.auth.routes import auth
from notificationEngine.trigger.routes import triggers
from notificationEngine.notification.routes import notification
from notificationEngine.user.routes import user
from notificationEngine.data.routes import data


app.register_blueprint(auth)
app.register_blueprint(data)
app.register_blueprint(user)
app.register_blueprint(triggers)
app.register_blueprint(notification)




# db = SQLAlchemy()
# bcrypt = Bcrypt()
# login_manager = LoginManager()


# def create_app(config_class=Config):
#     app = Flask(__name__)
#     app.config.from_object(Config)

#     db.init_app(app)
#     bcrypt.init_app(app)
#     login_manager.init_app(app)

#     from notificationEngine.auth.routes import auth
#     from notificationEngine.trigger.routes import triggers
#     # from notificationEngine.notification.routes import notification

#     app.register_blueprint(auth)
#     app.register_blueprint(triggers)
#     # app.register_blueprint(notification)

#     return app
