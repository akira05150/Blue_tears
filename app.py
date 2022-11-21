from detection import *
from flask import Flask, render_template, Response
from time import sleep

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

def detect():
    while True:
        frame = get_frame()
        yield (b'--frame\r\n'
        b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        sleep(0.01)

@app.route("/video_feed", methods=['GET'])
def video_feed():
    return Response(detect(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6200)
