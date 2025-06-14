from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello and welcom to FlaSH's CI/CD!"
