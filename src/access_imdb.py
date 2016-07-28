"""Module for accesing imdb."""
from imdb import IMDb, IMDbError


class AccessImdb():
    """Class for accesing imdb apis."""

    def __init__(self):
        """Method: Initialization- get imdb handle."""
        try:
            self.imdb = IMDb()
        except IMDbError, err:
            print err

    def get_movie_data(self, movie_name):
        """Method: get movie data for the movie."""
        try:
            imdb_movie_data_d = self.imdb.search_movie(movie_name)[0]
            self.imdb.update(imdb_movie_data_d)
            imdb_movie_data_d.data
        except IMDbError, err:
            print err
        return imdb_movie_data_d
