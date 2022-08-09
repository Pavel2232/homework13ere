import json

from flask import Blueprint

from app.movie.dao.movie_dao import MovieDAO

movie_blueprint = Blueprint('movie_blueprint', __name__)



@movie_blueprint.route("/movie/<title>")
def page_title(title):
    """ Данные про фильм """
    result = MovieDAO().get_movie_by_title(title)
    return [json.dumps(results.by_title).split(",") for results in result]


@movie_blueprint.route("/movie/<int:year>/to/<int:two_year>")
def movie_by_two_year(year,two_year):
    """Поиск по диапозону лет"""
    result = MovieDAO().get_movie_by_year(year,two_year)
    return  [json.dumps(results.by_two_year).split(",") for results in result]


@movie_blueprint.route("/rating/children")
def page_children():
    result = MovieDAO().get_movie_by_rating("g")
    return  [json.dumps(results.by_rating).split(",") for results in result]

@movie_blueprint.route("/rating/family")
def page_family():
    result = MovieDAO().get_movie_by_rating("g" or "pg" or"pg-13" )
    return  [json.dumps(results.by_rating).split(",") for results in result]


@movie_blueprint.route("/rating/adult")
def page_adult():
    result = MovieDAO().get_movie_by_rating("r" or "nc-17")
    return [json.dumps(results.by_rating).split(",") for results in result]

@movie_blueprint.route("/genre/<genre>")
def genre_page(genre):
    result = MovieDAO().get_top_movie_by_listed_in(genre)
    return [json.dumps(results.by_genre).split(",") for results in result]
