from detect_main import *
# import cv2
import os
from flask import Flask, render_template, Response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

def detect(detect_main):
    while True:
        frame = detect_main.detect_main()
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route("/detect")
def main():
    return Response(detect(), mimetype='multipart/x-mixed-replace; boundary=frame')

"""
def main():
    detect_main() 
"""

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    main()
    