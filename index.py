from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, flask</p>"

@app.route("/test")
def hello_test():
    return "<p>Hello, test</p>"