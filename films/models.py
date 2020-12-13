from films import db, ma
from marshmallow import Schema, fields, validate, ValidationError
from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True)
    password = db.Column(db.String(12))

    def __repr__(self):
        return f"User(id: '{self.id}', name: '{self.username}, description: '{self.password}')"


class UserSchema(ma.Schema):
    id = fields.Integer(allow_none=True)
    username = fields.Str(validate=validate.Length(min=1, max=32))
    password = fields.Str(validate=validate.Length(min=1, max=12))

    class Meta:
        model = User


class Genre(db.Model):
    __tablename__ = 'genre'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    description = db.Column(db.Text, index=True, unique=True)

    def __repr__(self):
        return f"Genre(id: '{self.id}', name: '{self.name}, description: '{self.description}')"


class GenreSchema(ma.Schema):
    id = fields.Integer(allow_none=True)
    name = fields.Str(validate=validate.Length(min=1, max=64))
    description = fields.Str(validate=validate.Length(min=1, max=200))

    class Meta:
        model = Genre


class Film(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.Text, nullable=False)
    duration = db.Column(db.DateTime, default=datetime.utcnow)
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'), nullable=False)

    def __repr__(self):
        return f"Film(id: '{self.id}', name: '{self.name}, description: '{self.description}', " \
               f"duration: '{self.duration}', genre_id: '{self.genre_id}')"


class FilmSchema(ma.Schema):
    id = fields.Integer(allow_none=True)
    name = fields.Str(validate=validate.Length(min=1, max=64))
    description = fields.Str(validate=validate.Length(min=1, max=400))
    genre_id = fields.Integer(required=True)
    duration = fields.DateTime(allow_none=True)

    class Meta:
        model = Film


class Session(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    film_id = db.Column(db.Integer, db.ForeignKey('film.id', ondelete="cascade"), nullable=False, unique=True)
    start_time = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"Session(id: '{self.id}', film_id: '{self.film_id}, start_time: '{self.start_time}')"


class SessionSchema(ma.Schema):
    id = fields.Integer(allow_none=True)
    film_id = fields.Integer(required=True)


class Hall(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    places = db.Column(db.Integer, index=True, unique=True)
    session_id = db.Column(db.Integer, db.ForeignKey('session.id', ondelete="cascade"), nullable=False, unique=True)

    def __repr__(self):
        return f"Hall(id: '{self.id}', places: '{self.places}, session_id: '{self.session_id}')"


class HallSchema(ma.Schema):
    id = fields.Integer(allow_none=True)
    places = fields.Integer(required=True)
    session_id = fields.Integer(required=True)
