class Movie():

    def __init__(self,title = None, country = None, releasy_year = 0, description = None, rating = None):
        self.title = title
        self.country = country
        self.release_year = releasy_year
        self.descriprion = description
        self.rating = rating


    def __repr__(self):
        return f"{self.title, self.country, self.release_year, self.descriprion}"