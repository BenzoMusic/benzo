from flask import Flask, jsonify, request
from flask_socketio import SocketIO
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

# Временное хранилище ссылок (в памяти)
soundcloud_links = {}

@app.route('/get_links', methods=['GET'])
def get_links():
    user_id = request.args.get('user_id')
    if user_id in soundcloud_links:
        return jsonify(soundcloud_links[user_id])
    return jsonify([])

@app.route('/add_link', methods=['POST'])
def add_link():
    data = request.json
    user_id = data['user_id']
    link = data['link']

    if user_id not in soundcloud_links:
        soundcloud_links[user_id] = []

    if link not in soundcloud_links[user_id]:
        soundcloud_links[user_id].append(link)
        socketio.emit('link_list_update', soundcloud_links[user_id], room=user_id)

    return jsonify({"status": "success"})

@app.route('/clear_links', methods=['POST'])
def clear_links():
    user_id = request.json['user_id']
    if user_id in soundcloud_links:
        del soundcloud_links[user_id]
    return jsonify({"status": "success"})

@socketio.on('connect')
def handle_connect():
    user_id = request.args.get('user_id')
    if user_id:
        print(f"User {user_id} connected")
        socketio.emit('link_list_update', soundcloud_links.get(user_id, []), room=user_id)

@socketio.on('disconnect')
def handle_disconnect():
    user_id = request.args.get('user_id')
    if user_id:
        print(f"User {user_id} disconnected")
        if user_id in soundcloud_links:
            del soundcloud_links[user_id]

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
