from films import app, db, ma
from flask import jsonify, request
from .models import *

genre_schema = GenreSchema()
genre_schemas = GenreSchema(many=True)


@app.route("/genre", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        all_genres = Genre.query.all()
        return genre_schemas.jsonify(all_genres)
    else:
        name = request.json['name']
        description = request.json['description']
        g = Genre(name=name, description=description)
        genre_data = genre_schema.dump(g)
        try:
            GenreSchema().load(genre_data)
            db.session.add(g)
            db.session.commit()
            return genre_schema.jsonify(g)

        except ValidationError as err:
            print("error")
            return jsonify(message=err.messages, status=405)  #


@app.route("/genre/<genre_id>", methods=['GET'])
def get_genre(genre_id):
    genre = Genre.query.get(genre_id)
    return genre_schema.jsonify(genre)


@app.route("/genre/<genre_id>", methods=['DELETE'])
def delete_genre(genre_id):
    genre = Genre.query.get(genre_id)
    db.session.delete(genre)
    db.session.commit()
    return genre_schema.jsonify(genre)
