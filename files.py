from flask import request, jsonify, render_template
import os
import json
from flask_sqlalchemy import SQLAlchemy
import uuid
from models import *
from datetime import datetime

@app.route('/get_files', methods=['POST'])
def get_files():
  user_id = request.json.get('user_id')  # Assume client sends user_id in JSON
  if not user_id:
      return jsonify({'error': 'User ID not provided'}), 400
  
  # Assuming files are stored in a folder named after user_id
  user_path = os.path.join('users',str(user_id),'files','file_index.json')
  print(user_path)

  # Read all .txt files in the user's folder
  if os.path.exists(user_path):
    try:
      with open(user_path, 'r') as f:
        data = json.load(f)
        return jsonify(data)
    except FileNotFoundError:
      return jsonify({'error': 'File not found'}), 404
    except json.JSONDecodeError:
      print("'JSON decoding error")
      return jsonify({'error': 'JSON decoding error'}), 500
  else:
    return jsonify({'error': 'User folder not found'}), 404


@app.route('/open_file', methods = ['GET', 'POST'])
def open_file():
  user = request.args.get('user')
  resource_id = request.args.get('resource_id')

  file = File.query.filter_by(guid=resource_id).first()
  if not file:
      return jsonify({'error': 'File not found'}), 404
    
  return render_template('article.html', user=user, resource_id=file.guid, name = file.name, publish_time = file.publish_time, content = file.content )

@app.route('/save_file', methods = ['POST'])
def save_file():
    textName = request.json.get('name') 
    user = request.json.get('user')
    content = request.json.get('content')
    file_guid = str(uuid.uuid4())
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    #img_str = 
    new_file = File(
        guid=file_guid,
        name=textName,
        user_name=user,
        publish_time = current_time,
    )
    db.session.add(new_file)
    db.session.commit()

    return jsonify({'message': 'File saved successfully', 'guid': file_guid}), 200