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

@socketio.on('connect')
def handle_connect():
    socketio.emit('state_update', player_state)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)