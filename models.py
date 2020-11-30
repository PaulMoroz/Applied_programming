from app import db
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
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'))
    #genre = db.relationship('Genre', cascade="all, delete", backref=db.backref('film', lazy=True))

    def __repr__(self):
        return f"Film(id: '{self.id}', name: '{self.name}, description: '{self.description}')" \
               f"duration: '{self.duration}')"


class Session(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    film_id = db.Column(db.Integer, db.ForeignKey('film.id', ondelete="cascade"), nullable=False, unique=True)
    start_time = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Session {}>'.format(self.body)


class Hall(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    places = db.Column(db.Integer, index=True, unique=True)
    session = db.Column(db.PickleType, nullable=True)

#session = db.relationship('Session', cascade="all, delete", backref=db.backref('film', lazy=True))
#session = db.Column(db.Array, db.ForeignKey('session', ondelete="cascade"), nullable=False, unique=True)
