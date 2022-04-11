from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt

# time module
from datetime import datetime
from datetime import timedelta
from datetime import timezone

# jwt module
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/bookshelf"
mongo = PyMongo(app)
# bycrypt
bcrypt = Bcrypt(app)

# Setup the Flask-JWT-Extended extension
app.config['JSON_SORT_KEYS'] = False
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=30)
app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
jwt = JWTManager(app)

# route
from app.books.route import *
from app.kafka.route import *