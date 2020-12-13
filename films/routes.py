from films import app, db, ma, bcrypt
from flask import jsonify, request, make_response
from .models import *

genre_schema = GenreSchema()
genre_schemas = GenreSchema(many=True)

film_schema = FilmSchema()
film_schemas = FilmSchema(many=True)

user_schema = UserSchema()
user_schemas = UserSchema(many=True)


@app.route("/user", methods=['GET', 'POST'])
def get_add_user():
    if request.method == 'GET':
        all_users = User.query.all()
        return user_schemas.jsonify(all_users)
    # POST method
    else:
        query_username = request.args.get('username')  # query parameters
        query_pass = request.args.get('password')

        if User.query.filter_by(username=query_username).first() is not None:  # if user is already registered
            return jsonify(message='user with same username exists', status=403)
        else:  # register if is not
            print('does not exists')
            # checking if data is valid before hashing, because it will change the pword length
            u = User(username=query_username, password=query_pass)
            user_data = user_schema.dump(u)
            try:
                UserSchema().load(user_data)
                h_query_pass = bcrypt.generate_password_hash(query_pass)  # hashing a password here
                u = User(username=query_username, password=h_query_pass)
                db.session.add(u)
                db.session.commit()
                return user_schema.jsonify(u)
            except ValidationError as err:
                return jsonify(message=err.messages, status=405)


@app.route("/film", methods=['GET', 'POST'])
def get_add_films():
    if request.method == 'GET':
        all_films = Film.query.all()
        return film_schemas.jsonify(all_films)
    else:
        name = request.json['name']
        description = request.json['description']
        duration = request.json['duration']
        genre_id = request.json['genre_id']
        f = Film(name=name, description=description, duration=duration, genre_id=genre_id)
        film_data = film_schema.dump(f)
        try:
            FilmSchema().load(film_data)
            db.session.add(f)
            db.session.commit()
            return film_schema.jsonify(f)
        except ValidationError as err:
            return jsonify(message=err.messages, status=405)


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
            return jsonify(message=err.messages, status=405)


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
