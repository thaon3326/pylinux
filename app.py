from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, I am Thao!"
    
@app.route("/test_git")
def hello():
    return "Hello, test git python cua toi"
    