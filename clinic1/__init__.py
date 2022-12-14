from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import cloudinary


app = Flask(__name__)
app.secret_key = 'vdbusiy83e2@'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456789@localhost/hospital-management?charset=utf8mb4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
cloudinary.config(
  cloud_name = "dpnkep1km",
  api_key = "832627139245734",
  api_secret = "Bu9HQ3UlNwt62PXYq-STmGkI9Zc"
)

login = LoginManager(app=app)

db = SQLAlchemy(app=app)
