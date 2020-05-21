from flask import Flask
import json
from flask import request, jsonify
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello narasimha!"

# app.run()
