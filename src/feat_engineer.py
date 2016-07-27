#!/usr/bin/python

# Import the imdb package.
import imdb
import sys
sys.path.append('../../BoxOfficeMojo/boxofficemojoAPI')
from movie import *
from boxofficemojo import BoxOfficeMojo
from base import MovieBase

import helper as hlp

def init_moviedb():
    box_office_mojo = BoxOfficeMojo()
    box_office_mojo.crawl_for_urls()


def create_movie_list():
    movies_in_given_range = []
    for k, v in take(20, box_office_mojo.movie_urls.iteritems()):
        movie = box_office_mojo.get_movie_summary(k)
        movie_data = movie.to_json()  # string
        d = json.loads(movie_data)  # dict
        date = d['Release Date'].split(' ')

        if ((len(date)) == 3 and (int(date[2]) in range(2006, 2016))):
            movies_in_given_range.append(k)
            # put this in the database
