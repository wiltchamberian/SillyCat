from flask import request, jsonify, render_template
import os
import json
from flask_sqlalchemy import SQLAlchemy
import uuid
from models import *
from helper import *
from initial_env import *

@app.route('/get_file_list', methods=['GET', 'POST'])
def get_file_list():
  try:
    user = request.json.get("user")
    files = File.query.filter_by(user = user).with_entities(File.title, File.guid).all()
    files_list = [{'title': file.title, 'guid': file.guid} for file in files]
    return jsonify(files_list)
  except Exception as e:
    return jsonify({'error': str(e)}), 500

@app.route('/open_file', methods = ['GET', 'POST'])
def open_file():
  user = request.args.get('user')
  resource_id = request.args.get('resource_id')

  file = File.query.filter_by(guid=resource_id).first()
  if not file:
    return jsonify({'error': 'File not found'}), 404
    
  return render_template('article.html', file = file)

@app.route('/upsert_file', methods = ['POST'])
def upsert_file():
  title = request.json.get('title') 
  user = request.json.get('user')
  content = request.json.get('content')
  guid = request.json.get('guid')

  file_guid = None
  if(guid != None):
    file_guid = guid
    existing_file = File.query.filter_by(guid=file_guid, user_name=user).first()
    if existing_file:
      # 如果记录存在，更新 content 和其他字段（如果需要）
      existing_file.content = content
      existing_file.title = title  # 可选：更新其他字段
      existing_file.publish_time = current_time()  # 可选：更新发布时间
      db.session.commit()
  else:
    file_guid = str(uuid.uuid4())
    new_file = File(
        guid=file_guid,
        title=title,
        user=user,
        publish_time=current_time(),
        content=content
    )
    db.session.add(new_file)
    db.session.commit()

  return jsonify({'message': 'File saved successfully', 'guid': file_guid}), 200