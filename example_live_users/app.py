from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import os
import json
import sys



app = Flask(__name__)
socketio = SocketIO(app)

@socketio.on('connect')
def ws_connect():
    try:
        f = open("test.txt", "r")
        data = f.read()
        tem = {'counter': int(json.loads(data).get("counter")) + 1}
        f.close()
        emit('user', tem, broadcast=True)

        fw = open("test.txt", "w")
        fw.write(json.dumps(tem))
        fw.close()
        emit('connect', tem, broadcast=True)

    except Exception as e:
        fw = open("test.txt", "w")
        fw.write(json.dumps({"counter": 0}))
        fw.close()
        emit('user', {'counter': 0}, broadcast=True)

@socketio.on('disconnect')
def ws_disconnect():
    f = open("test.txt", "r")
    data = f.read()
    tem = {'counter': int(json.loads(data).get("counter")) - 1}
    f.close()
    fw = open("test.txt", "w")
    fw.write(json.dumps(tem))
    fw.close()
    emit('user', tem, broadcast=True)

@app.route('/', methods=['GET', 'POST'])
def home():
    f = open("test.txt", "r")
    data = f.read()
    data = {'counter': int(json.loads(data).get("counter"))}
    return render_template("index.html", data=data)


if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0', port=5000)