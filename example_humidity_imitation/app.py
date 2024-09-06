from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import json
import time

app = Flask(__name__)
socketio = SocketIO(app)

def get_sensor_data():
    with open("log.json", "r") as file:
        data = json.load(file)
    return data

@socketio.on('connect')
def handle_connect():
    emit('sensor_update', get_sensor_data())

@socketio.on('request_update')
def handle_update_request():
    emit('sensor_update', get_sensor_data())

@app.route('/', methods=['GET'])
def home():
    return render_template("index.html", initial_data=get_sensor_data())

if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0', port=5000)