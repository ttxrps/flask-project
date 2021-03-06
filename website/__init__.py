from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
# call SQLAlchemy
db = SQLAlchemy()
# create database name
DB_NAME = "database.db"

# create function create app for main.py
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dsfjksdkjlflks'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    # import Blueprimt
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # import models
    from .models import User
    # create database
    create_database(app)

    # call LoginManager for check user login
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database')
