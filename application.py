from flask import Flask
import json
from flask import request, jsonify
app = Flask(__name__)

@app.route("/")
def hello():
    return "SUPERCOMPUTER MOCKING SERVICE"

def attributes():
    f = open("./attributes.json")
    data = json.load(f)
    f.close()
    return jsonify(data)
app.add_url_rule('/ufmRest/monitoring/attributes','attributes',attributes,'GET')


# app.run()
