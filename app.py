from sys import stdout
from makeup_artist import Makeup_artist
import logging
from flask import Flask, render_template, Response
from flask_socketio import SocketIO
from camera import Camera
from utils import base64_to_pil_image, pil_image_to_base64


app = Flask(__name__)
app.logger.addHandler(logging.StreamHandler(stdout))
app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = True
socketio = SocketIO(app)
camera = Camera()


@socketio.on('input image', namespace='/test')
def test_message(input):
    input = input.split(",")[1]
    camera.enqueue_input(input)
    #camera.enqueue_input(base64_to_pil_image(input))


@socketio.on('connect', namespace='/test')
def test_connect():
    app.logger.info("client connected")


@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


@app.route('/take_picture')
def take_picture():
    return print('I got clicked')

if __name__ == '__main__':
    socketio.run(app)
