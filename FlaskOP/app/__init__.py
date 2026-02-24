from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///country.db"
app.config["JWT_SECRET_KEY"] = "Divu"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)
basic_auth = HTTPBasicAuth()
jwt = JWTManager(app)

from app import auth
from app.controllers import country_controller,user_controller
from app import commands

