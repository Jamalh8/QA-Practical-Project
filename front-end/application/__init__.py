from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from os import getenv
# import pymysql

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI")
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)

from application import routes