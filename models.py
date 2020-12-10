from main import db
from datetime import datetime


class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    description = db.Column(db.Text, index=True, unique=True)

    def __repr__(self):
        return f"Genre(id: '{self.id}', name: '{self.name}, description: '{self.description}')"


class Film(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.Text, nullable=False)
    duration = db.Column(db.DateTime, default=datetime.utcnow)
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'), nullable=False)


class Session(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    film_id = db.Column(db.Integer, db.ForeignKey('film.id', ondelete="cascade"), nullable=False, unique=True)
    start_time = db.Column(db.DateTime, default=datetime.utcnow)


class Hall(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    places = db.Column(db.Integer, index=True, unique=True)
    session_id = db.Column(db.Integer, db.ForeignKey('session.id', ondelete="cascade"), nullable=False, unique=True)


