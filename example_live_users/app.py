from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import os
import json
import sys

app = Flask(__name__)
socketio = SocketIO(app)

@socketio.on('connect')
def ws_connect():
    with open("log.json", "r") as file:
        data = json.load(file)
    updated_counter = {'counter': data['counter'] + 1}
    emit('user', updated_counter, broadcast=True)

    with open("log.json", "w") as file:
        json.dump(updated_counter, file)
    emit('connect', updated_counter, broadcast=True)

@socketio.on('disconnect')
def ws_disconnect():
    with open("log.json", "r") as file:
        data = json.load(file)
    updated_counter = {'counter': data['counter'] - 1}
    with open("log.json", "w") as file:
        json.dump(updated_counter, file)
    emit('user', updated_counter, broadcast=True)

@app.route('/', methods=['GET', 'POST'])
def home():
    with open("log.json", "r") as file:
        data = json.load(file)
    return render_template("index.html", data=data)


if __name__ == '__main__':
    # Initialize counter to 0 when app is launched
    with open("log.json", "w") as file:
        json.dump({"counter": 0}, file)
    
    socketio.run(app, debug=True, host='0.0.0.0', port=5000)