class Movie():
    """Класс фильм"""
    """show_id, type,  title, director, cast, country, date_added, release_year,  rating, duration, duration_type, 
    listed_in, description """
    def __init__(self, show_id=None, type=None, title=None, director=None, cast=None, country=None, date_added=None, release_year = None, rating = None, duration = None, duration_type = None, listed_in = None, description = None):
        self.show_id = show_id
        self.type = type
        self.title = title
        self.director = director
        self.cast = cast
        self.country = country
        self.date_added = date_added
        self.release_year = release_year
        self.rating = rating
        self.duration = duration
        self.duration_type = duration_type
        self.listed_in = listed_in
        self.descriprion = description
        """Выводы под запросы"""
        self.by_title = f"title:{title} ,country: {country} ,release_year:{release_year} ,listed_in: {listed_in} ,description: {description}"
        self.by_two_year = f"title: {title},release_year: {release_year}"
        self.by_rating = f"title:{title}, rating: {rating}, description: {description}"
        self.by_genre = f"title:{title},  description: {description}"

    def __repr__(self):
        return f"{self.title}"