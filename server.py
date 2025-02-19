from flask import Flask, request, jsonify
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

# Текущее состояние плеера
player_state = {
    "current_track": None,
    "is_playing": False,
    "position": 0
}

# Список доступных треков
tracks = []

@app.route('/update_state', methods=['POST'])
def update_state():
    global player_state
    data = request.json
    player_state.update(data)
    socketio.emit('state_update', player_state)
    return jsonify({"status": "success"})

@app.route('/get_state', methods=['GET'])
def get_state():
    return jsonify(player_state)

@app.route('/add_track', methods=['POST'])
def add_track():
    global tracks
    data = request.json
    tracks.append(data)
    socketio.emit('track_list_update', tracks)  # Отправляем обновленный список треков всем
    return jsonify({"status": "success"})

@app.route('/get_tracks', methods=['GET'])
def get_tracks():
    return jsonify(tracks)

@socketio.on('connect')
def handle_connect():
    socketio.emit('state_update', player_state)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, allow_unsafe_werkzeug=True)
