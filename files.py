from flask import request, jsonify
import os
import json

def get_the_files():
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
