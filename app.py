from flask import Flask, render_template, request, redirect
from waitress import serve
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lab.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)





@app.route('/')
def start():
    return "Empty page"


@app.route('/api/v1/hello-world-16')
def greeting():
    return "Hello World 16"


@app.route('/film', methods=['POST', 'GET'])
def film():
    if request.method == "POST":
        name = request.form['name']
        description = request.form['description']
        genre = request.form['genre']
        duration = request.form['duration']

        film = Film(name=name, description=description, genre=genre, duration=duration)

        try:
            db.session.add(film)
            db.session.commit()
            return redirect('/')
        except:
            return "Error"
    else:
        return render_template("film.html")


if __name__ == "__main__":
   serve(app, host='0.0.0.0', port=5000)


   # app.run(debug=True)  # для виводу помилок
   #http://localhost:5000/api/v1/hello-world-1
   #waitress-serve --port=5000 app:app
   #curl -v -XGET http://localhost:5000/api/v1/hello-world1