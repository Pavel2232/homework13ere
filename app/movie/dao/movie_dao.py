import json
from config import DATA_DIR
from app.movie.dao.movie import Movie
import sqlite3

DATA_PATH = DATA_DIR.joinpath("netflix.db")


class MovieDAO:

    @property
    def get_movie(self) -> list:
        """Таблица получается в списке кортежей"""
        with sqlite3.connect(DATA_PATH) as connection:
            cursor = connection.cursor()
            query = """
                    SELECT *
                    FROM netflix
            """
            cursor.execute(query)
            results = cursor.fetchall()
            return results

    def load_movie(self) -> list[Movie]:
        """Получаем классы фильмов"""
        """0-show_id,1-type,2-title,3-director,4-cast,5-country,6-date_added,7-release_year,8-rating,9-duration,
        10-duration_type,11-listed_in,12-description """
        movies = []
        for movie in self.get_movie:
            movies.append(Movie(
                movie[0],
                movie[1],
                movie[2],
                movie[3],
                movie[4],
                movie[5],
                movie[6],
                movie[7],
                movie[8],
                movie[9],
                movie[10],
                movie[11],
                movie[12]
            ))
        return movies

    def get_movie_by_title(self, title) -> list[Movie]:
        """Получаем фильм по названию"""
        list = []
        for movies in self.load_movie():
            if title.lower() in movies.title.lower():
                list.append(movies)
        return list

    def get_movie_by_year(self, first_year, two_year) -> list[Movie]:
        """Получаем фильмы по диапазону выпуска"""
        list = []
        for movies in self.load_movie():
            if first_year or two_year == movies.release_year:
                list.append(movies)
        return list

    def get_movie_by_rating(self, rating) -> list[Movie]:
        """Получаем фильмы по возрастному рейтингу"""
        list = []
        for movies in self.load_movie():
            if rating.lower() in movies.rating.lower():
                list.append(movies)
        return list

    def get_top_movie_by_listed_in(self, listed_in) -> list[Movie]:
        """Получение топ 10 самых свежих фильмов по жанру"""
        list = []
        for movies in self.load_movie():
            if listed_in.lower() in movies.listed_in.lower():
                list.append(movies)

        def sort_key(s):
            """Сортировка по дате"""
            return s.release_year

        result = sorted(list, key=sort_key)
        return result

    def get_movie_by_two_actor(self, first_act, second_actor) -> list[Movie]:
        """Получение фильма где играет оба полученных актера"""
        list = []
        for movies in self.load_movie():
            if first_act.lower() and second_actor.lower() in movies.cast.lower():
                list.append(movies)
        return list

    def get_movie_by_type_yeaer_listed_in(self, type, year, listed_in) -> str:
        """Получаем на выходе список названий картин с их описаниями в JSON"""
        list = []
        for movies in self.load_movie():
            if type.lower() in movies.type.lower() and year == movies.release_year and listed_in.lower() in movies.listed_in.lower():
                list.append(movies)
        return [json.dumps(lists.by_genre) for lists in list]
