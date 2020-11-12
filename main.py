from flask import Flask
from classes import *
cinema = Cinema()
app = Flask(__name__)

@app.route("/api/v1/hello-world")
def index():
    return "Hello,World! "

if __name__=="__main__":
    app.run(debug=True,use_reloader=False)
