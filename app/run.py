from flask import Flask
from app.movie.views import movie_blueprint

app = Flask(__name__)

app.register_blueprint(movie_blueprint)

if __name__ == "__main__":
    app.run()
