from films import app, db, ma
from flask import jsonify, request, make_response
from .models import *

genre_schema = GenreSchema()
genre_schemas = GenreSchema(many=True)


@app.route("/genre", methods=['GET', 'POST'])
def get_add_genres():
    if request.method == 'GET':
        all_genres = Genre.query.all()
        return genre_schemas.jsonify(all_genres)
    else:
        # print('beep')
        # query_pass = request.args.get('password')
        # print("Q:PASS", query_pass)

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
            return jsonify(message=err.messages, status=405)  #


@app.route("/genre/<int:genre_id>", methods=['GET'])
def get_genre(genre_id):
    genre = Genre.query.get(genre_id)
    if genre is None:
        return jsonify(message='genre not found', status=404)
    return genre_schema.jsonify(genre)


@app.route("/genre/<int:genre_id>", methods=['PUT'])
def update_genre(genre_id):
    genre = Genre.query.get(genre_id)
    if genre is None:
        return jsonify(message='genre not found', status=404)
    req_data = request.get_json()
    try:
        req_data = genre_schema.dump(req_data)
        g = GenreSchema().load(req_data)
        genre.name = g['name']
        genre.description = g['description']
        db.session.commit()
        return jsonify(req_data)
    except ValidationError as err:
        return jsonify(message=err.messages, status=405)


@app.route("/genre/<int:genre_id>", methods=['DELETE'])
def delete_genre(genre_id):
    genre = Genre.query.get(genre_id)
    if genre is not None:
        db.session.delete(genre)
        db.session.commit()
        return genre_schema.jsonify(genre)
    else:
        return jsonify(message='genre not found', status=404)
        # return make_response('genre not found', 404)
