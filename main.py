from flask import Flask

a = input("Enter your variant")
app = Flask(__name__)

@app.route("/api/v1/hello-world-"+a)
def index():
    return "Hello,World! "+a

if __name__=="__main__":
    app.run(debug=True,use_reloader=False)
