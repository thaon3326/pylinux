from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, I am Thao!"
    
@app.route("/test_git")
def test_git():
    return "Hello, test git python cua toi"
    
@app.route("/add_branch")
def add_branch():
    return "Hello! I just add new branch in git"
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)