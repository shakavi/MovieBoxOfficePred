"""Module containing constant sql statements."""

INSERT_INTO_MOVIES_STMT = '''
INSERT INTO moviesattr(movie_id, title, release_date,
 runtimes, country, languages, Budget, rating, mpaa, plot)
VALUES(?, ?, ?, ?, ? , ?, ?, ?, ?, ?);'''

INSERT_INTO_MOVIE_ATTR_STMT = '''
INSERT INTO moviesattr(movie_id, attr_key, attr_value)
VALUES(?, ?, ?)'''

INSERT_IN_MOVIEDB_STMT = '''
INSERT INTO moviesattr(movie_id, week_number, average_per_theatre,
 gross, rank, theaters, date_of_week, week_over_week_change)
VALUES(?, ?, ?, ?, ? , ?, ?, ?)'''


class _Const(object):
    # @constant
    def INSERT_INTO_MOVIES():
        return INSERT_INTO_MOVIES_STMT

    def INSERT_INTO_MOVIE_ATTR():
        return INSERT_INTO_MOVIE_ATTR_STMT

    def INSERT_IN_MOVIEDB():
        return INSERT_IN_MOVIEDB_STMT
