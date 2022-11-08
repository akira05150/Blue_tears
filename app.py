from detect_gesture import *
#from flask import Flask, render_template, request
"""
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
"""
def main():
    detect_hands_gesture()

if __name__ == '__main__':
	#port = int(os.environ.get('PORT', 5000))
    #app.run(host='0.0.0.0', port=port)
    main()
    