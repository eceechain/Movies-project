#!/usr/bin/env python3

from random import choice as rc
from faker import Faker
from app import app
from models import Movie, User, Review, db

fake = Faker()

def seed_movies():
    with app.app_context():
        # Delete existing data
        Movie.query.delete()
        User.query.delete()
        Review.query.delete()

        # Seed Movies
        movies = []
        genres = ['Action', 'Comedy', 'Drama', 'Sci-Fi', 'Horror']
        for _ in range(150):
            movie = Movie(
                title=fake.catch_phrase(),
                genre=rc(genres),
                release_year=fake.year(),
                director=fake.name(),
            )
            movies.append(movie)

        # Seed Users
        users = []
        for i in range(150):
            user = User(
                username=fake.user_name(),
                bio=fake.text(),
                is_active=True,
            )
            users.append(user)

        # Seed Reviews
        reviews = []
        for _ in range(300):
            movie = rc(movies)
            user = rc(users)
            review = Review(
                content=fake.paragraph(),
                comments=fake.paragraph(),
                rating=rc(range(1, 6)),  # Random rating from 1 to 5
                
            )
            reviews.append(review)

        db.session.add_all(movies + users + reviews)
        db.session.commit()

if __name__ == "__main__":
    seed_movies()
