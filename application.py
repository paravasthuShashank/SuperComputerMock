from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Kishore!"

app.run(ssl_context = 'adhoc')
