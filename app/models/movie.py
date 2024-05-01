
from app.db import BaseModel

class Movie(BaseModel):

    SHEET_NAME = "movies"

    COLUMNS = ["title", "director", "year"]

    SEEDS = [
        {"title": "The Lord of the Rings", "director": "Peter Jackson", "year": 2001},
        {"title": "Perros Amorosos", "director": "Alejandro Inarritu", "year": 2001},
        {"title": "Wild Tales", "director": "Ricardo Darin", "year": 2017},
        {"title": "El Secreto  de sus Ojos", "director": "Ricardo Darin", "year": 2009},
        {"title": "Roma", "director": "Alfonso Cuaron", "year": 2018},
        {"title": "Ciudad de Dios", "director": "Neymar Jr", "year": 2002},
        {"title": "Cronicas", "director": "Damian Alcazar", "year": 1995},
        {"title": "El Laberinto del Fauno", "director": "Guillermo del Toro", "year": 2006},
        {"title": "Selana", "director": "Selena", "year": 1997},
        {"title": "Im no longer here", "director": "Juan David Garcia", "year": 2005},
        {"title": "Paraiso Travel", "director": "Simon Brand", "year": 2004},
        {"title": "Poya", "director": "Hetores", "year": 2000},
    ]


if __name__ == "__main__":

    movies = Movie.all()
    print("FOUND", len(movies), "MOVIES")
    if any(movies):
        for movie in movies:
            print(movie.title, movie.director, movie.year)
    else:
        Movie.seed()

