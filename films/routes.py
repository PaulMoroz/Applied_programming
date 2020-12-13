from films import app, db, ma, bcrypt
from flask import jsonify, request, make_response
from .models import *

genre_schema = GenreSchema()
genre_schemas = GenreSchema(many=True)

film_schema = FilmSchema()
film_schemas = FilmSchema(many=True)

user_schema = UserSchema()
user_schemas = UserSchema(many=True)

session_schema = SessionSchema()
session_schemas = SessionSchema(many=True)


# http://127.0.0.1:5000/user/ to get. or send a json to post
@app.route("/user/", methods=['GET', 'POST'])
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
                return jsonify(message='user was created', status=201)
                # return user_schema.jsonify(u)
            except ValidationError as err:
                return jsonify(message=err.messages, status=405)


# http://127.0.0.1:5000/user/login/?username=taras&password=admin
@app.route("/user/login/", methods=['POST'])
def login():
    query_username = request.args.get('username')  # query parameters
    query_pass = request.args.get('password')
    u = User.query.filter_by(username=query_username).first()
    if u is not None:
        if bcrypt.check_password_hash(u.password, query_pass):
            return jsonify(message='login approved', status=200)
    return jsonify(message='wrong username or password', status=403)


# http://127.0.0.1:5000/user/1
@app.route("/user/<int:user_id>", methods=['GET'])
def get_user(user_id):
    u = User.query.get(user_id)
    if u is None:
        return jsonify(message='user not found', status=404)
    return user_schema.jsonify(u)


# http://127.0.0.1:5000/user/1
@app.route("/user/<int:user_id>", methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if user is not None:
        db.session.delete(user)
        db.session.commit()
        return user_schema.jsonify(user)
    else:
        return jsonify(message='user not found', status=404)


# http://127.0.0.1:5000/film/ to get. or send a json to post
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
            # return film_schema.jsonify(f)
            return jsonify(message='film was added', status=201)
        except ValidationError as err:
            return jsonify(message=err.messages, status=405)


# http://127.0.0.1:5000/film/1
@app.route("/film/<int:film_id>", methods=['GET'])
def get_film(film_id):
    film = Film.query.get(film_id)
    if film is None:
        return jsonify(message='film not found', status=404)
    return film_schema.jsonify(film)


@app.route("/film/<int:film_id>", methods=['PUT'])
def update_film(film_id):
    film = Film.query.get(film_id)
    if film is None:
        return jsonify(message='film not found', status=404)
    req_data = request.get_json()
    try:
        req_data = film_schema.dump(req_data)
        f = FilmSchema().load(req_data)
        film.name = f['name']
        film.description = f['description']
        film.genre_id = f['genre_id']
        # film.duration = f['duration']
        db.session.commit()
        return jsonify(req_data)
    except ValidationError as err:
        return jsonify(message=err.messages, status=405)


# http://127.0.0.1:5000/film/1
@app.route("/film/<int:film_id>", methods=['DELETE'])
def delete_film(film_id):
    film = Film.query.get(film_id)
    if film is not None:
        db.session.delete(film)
        db.session.commit()
        return film_schema.jsonify(film)
    else:
        return jsonify(message='genre not found', status=404)


@app.route("/hall/session", methods=['GET', 'POST'])
def get_add_sessions():
    if request.method == 'GET':
        all_sessions = Session.query.all()
        return session_schemas.jsonify(all_sessions)
    else:
        film_id = request.json['film_id']
        start_time = request.json['start_time']
        s = Session(film_id=film_id, start_time=start_time)
        session_data = session_schema.dump(s)
        try:
            SessionSchema().load(session_data)
            db.session.add(s)
            db.session.commit()
            return jsonify(message='session was added', status=201)
        except ValidationError as err:
            return jsonify(message=err.messages, status=405)


@app.route("/hall/<int:session_id>", methods=['GET'])
def get_session(session_id):
    session = Session.query.get(session_id)
    if session is None:
        return jsonify(message='session not found', status=404)
    return session_schema.jsonify(session)


@app.route("/hall/<int:session_id>", methods=['PUT'])
def update_session(session_id):
    session = Session.query.get(session_id)
    if session is None:
        return jsonify(message='session not found', status=404)
    req_data = request.get_json()
    try:
        req_data = session_schema.dump(req_data)
        s = SessionSchema().load(req_data)
        session.film_id = s['film_id']
        session.start_time = s['start_time']
        db.session.commit()
        return jsonify(req_data)
    except ValidationError as err:
        return jsonify(message=err.messages, status=405)


@app.route("/hall/<int:session_id>", methods=['DELETE'])
def delete_session(session_id):
    session = Session.query.get(session_id)
    if session is not None:
        db.session.delete(session)
        db.session.commit()
        return session_schema.jsonify(session)
    else:
        return jsonify(message='session not found', status=404)


@app.route("/genre", methods=['GET', 'POST'])
def get_add_genres():
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
            return jsonify(message='genre was added', status=201)
            # return genre_schema.jsonify(g)
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
