from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'  # SQLite 数据库
db = SQLAlchemy(app)


class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    guid = db.Column(db.String(36), nullable=False, unique=True)
    name = db.Column(db.String(255), nullable=False)
    user_name = db.Column(db.String(255),nullable= False)
    img = db.Column(db.String(255), default='')
    publish_time = db.Column(db.String(32))
    content = db.Column(db.Text) 

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

# 创建数据库表
db.create_all()
