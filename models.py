from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def initial_db(app):
  db.init_app(app)

class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    guid = db.Column(db.String(36), nullable=False, unique=True)
    title = db.Column(db.String(255), nullable=False)
    user = db.Column(db.String(255),nullable= False)
    img = db.Column(db.String(255), default='')
    publish_time = db.Column(db.String(32))
    content = db.Column(db.Text) 

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    #password = db.Column(db.String(255), nullable=False)

