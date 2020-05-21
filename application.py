from flask import Flask,Response
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

def resources():
    f = open("./result.json")
    data = json.load(f)
    f.close()
    return jsonify(data)
app.add_url_rule('/ufmRest/resources/systems', 'resources', resources,'GET')

def start():
    response = Response()
    response.headers["Location"] = "https://supercomputermockserviceexample1.azurewebsites.net/ufmRest/monitoring/session/1000"
    return response
app.add_url_rule('/ufmRest/monitoring/start', 'start', start, 'POST')

def data():
    sessionFile = open('./session.txt','w')
    sessionFile.write(str(1000))
    sessionFile.close()
    # sessionId = 10628
    f = open("./resultData.json")
    data = json.load(f)
    f.close()
    return jsonify(data)
app.add_url_rule('/ufmRest/monitoring/session/1000/data', 'data', data, 'GET')

def delete():
    return """delete page"""
sessionFile = open('./session.txt','r')
sessionId = sessionFile.read().strip()
sessionFile.close()
deleteUrl = '/ufmRest/monitoring/session/' + sessionId
app.add_url_rule(deleteUrl,'delete', delete)

# app.run()
