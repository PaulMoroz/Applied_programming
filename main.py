from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lab.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

#a = input("Enter your variant")


# @app.route("/api/v1/hello-world-"+a)
# def index():
#     return "Hello,World! "+a


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
