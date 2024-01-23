from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Movie(db.Model, SerializerMixin):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    genre = db.Column(db.String)
    image = db.Column(db.String)
    release_year = db.Column(db.Integer)
    director = db.Column(db.String)

    # Relationship
    reviews = db.relationship('Review', back_populates='movie', lazy=True)

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True)
    bio = db.Column(db.Text)
    is_active = db.Column(db.Boolean, default=True)

    # Relationship
    reviews = db.relationship('Review', back_populates='user', lazy=True)

class Review(db.Model, SerializerMixin):
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    comments = db.Column(db.Text)  # Corrected line here
    rating = db.Column(db.Integer)

    # Relationship
  # Review model
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.id', name='fk_review_movie_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', name='fk_review_user_id'))

    # Establishing bidirectional relationship
    movie = db.relationship('Movie', back_populates='reviews')
    user = db.relationship('User', back_populates='reviews')
