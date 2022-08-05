from app.movie.dao.movie import Movie
import sqlite3


class MovieDAO():


    def __init__(self):
        pass

    def get_movie(self)->list:
        pass
        with sqlite3.connect("../../netflix.db") as connection:
            cursor = connection.cursor()
            query = """
                    SELECT title,country, release_year, description , rating
                    FROM netflix
            """
            result = cursor.execute(query)
            results = cursor.fetchall()
            return results


    def load_movie(self)->list[Movie]:
        movies = []
        for movie in self.get_movie():
            movies.append(Movie(
                movie[0],
                movie[1],
                movie[2],
                movie[3],
                movie[4]
            ))
        return movies



    def get_movie_by_title(self,title)->list[Movie]:
        list = []
        for movies in self.load_movie():
            if title.lower() in movies.title.lower():
                list.append(movies)
        return list


    def get_movie_by_year(self,first_year,two_year ):
        list = []
        for movies in self.load_movie():
            if first_year or two_year == movies.release_year:
                list.append(movies)
        return list
 #       return title country release_year, description


    def get_movie_by_rating(self,rating):
        list = []
        for movies in self.load_movie():
            if rating.lower() in movies.rating.lower():
                list.append(movies)
        return list



#- G — нет возрастных ограничений.
# PG — желательно присутствие родителей.
#- PG-13 — для детей от 13 лет в присутствии родителей.
#- R — дети до 16 лет допускаются на сеанс только в присутствии родителей.
#- NC-17 — дети до 17 лет не допускаются.


s = MovieDAO()
#l = MovieDAO().load_movie()
#for i in l:
#    print(f"{i.__dict__}\n")

#print(f"{s.get_movie_by_year(2021,2020)[:100]}\n")