from flask import Flask, jsonify
import threading
import time

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(status="alive")

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = threading.Thread(target=run)
    t.start()

# Call this function in your main file to keep the app alive
keep_alive()