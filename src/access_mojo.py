"""Module for accesing BoxOfficeMojo."""
import json
import sys
sys.path.append('/Users/KavitaS/cohort4/project/BoxOfficeMojo')
import boxofficemojoAPI as bom
# from boxofficemojo import BoxOfficeMojo


class AccessMojo():
    """Class for accesing BoxOfficeMojo apis."""

    def __init__(self):
        """Method: Initialization- get imdb handle."""
        self.box_office_mojo = bom.BoxOfficeMojo()
        self.movie_urls = self.box_office_mojo.crawl_for_urls()
        print self.box_office_mojo.total_movies

    def get_movies(self, from_date, to_date):
        """Method: get all movies released during given time frame."""
        movies_in_given_range_l = []
        movie_count_i = 0
        mojo_movie_summary = self.box_office_mojo.get_movie_summary('Titanic')

        for movieid, movie in self.movie_urls.items():
            # print "name", movie

            # print "id", movieid

            # get the mojo movie data
            mojo_movie_summary = self.box_office_mojo.get_movie_summary(
                                                                    movieid)

            print mojo_movie_summary
            mojo_movie_data_s = mojo_movie_summary.to_json()  # string
            mojo_movie_data_d = json.loads(mojo_movie_data_s)  # dict

            date = mojo_movie_data_d['Release Date'].split(' ')
            if ((len(date)) == 3 and (
                    int(date[2]) in range(from_date, to_date))):
                movie_count_i += 1
                movies_in_given_range_l.append(movieid)
            print "No of movies in the range", movie_count_i
            return movie_count_i, movies_in_given_range_l

    def get_movie_data(self, movie_name):
        """Method: get movie data for the movie."""
        movie_summary = self.box_office_mojo.get_movie_summary(movie_name)
        return movie_summary.clean_data()

    def get_bo_weekly_revenue(self, movie_name):
        """Method: get weekly revenue for the movie."""
        weekly = self.box_office_mojo.get_weekly_summary(movie_name)
        return weekly.clean_data()
