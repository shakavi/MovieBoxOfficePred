CREATE_MOVIE_TBL = '''CREATE TABLE movies (
    movie_id   serial PRIMARY KEY,
    title      text NOT NULL DEFAULT "None",
    release_date date,
    runtimes    numeric NOT NULL DEFAULT 0,
    country     text NOT NULL DEFAULT "USA",
    languages   text NOT NULL DEFAULT "English",
    Budget      numeric NOT NULL DEFAULT 0,
    rating      numeric NOT NULL DEFAULT 0,
    mpaa        text NOT NULL DEFAULT 0,
    plot        text NOT NULL DEFAULT "plot"
);'''

INSERT_INTO_MOVIES = '''
INSERT INTO moviesattr(movie_id, title, release_date,
 runtimes, country, languages, Budget, rating, mpaa, plot)
VALUES(?, ?, ?, ?, ? , ?, ?, ?, ?, ?)'''

UPDATE MOVIES = """
UPDATE movies SET plot = %s WHERE movie_id = %s"""

CREATE_MOVIE_ATTR_TBL = '''CREATE TABLE moviesattr (
    movie_id  int REFERENCES movies (movie_id),
    attr_key  text NOT NULL,
    attr_value text NOT NULL,
    CONSTRAINT movie_actor_pkey PRIMARY KEY (movie_id, attr_key, attr_value)
);'''

INSERT_INTO_MOVIE_ATTR = '''
INSERT INTO moviesattr(movie_id, attr_key, attr_value)
VALUES(?, ?, ?)'''


CREATE_BOXOFFICE_COL_TBL = '''CREATE TABLE box_office_col (
    movie_id            int REFERENCES movies (movie_id),
    week_number         numeric NOT NULL DEFAULT 0,
    average_per_theatre numeric NOT NULL DEFAULT 0,
    gross               numeric NOT NULL DEFAULT 0,
    rank                numeric NOT NULL DEFAULT 0,
    theaters            numeric NOT NULL DEFAULT 0,
    date_of_week        date,
    week_over_week_change numeric NOT NULL DEFAULT 0,
    CONSTRAINT movie_actor_pkey PRIMARY KEY (movie_id, week_number)
);'''



INSERT_IN_MOVIEDB = '''
INSERT INTO moviesattr(movie_id, week_number, average_per_theatre,
 gross, rank, theaters, date_of_week, week_over_week_change)
VALUES(?, ?, ?, ?, ? , ?, ?, ?)'''



'''
"average_per_theatre": 11848.0,
            "gross": 32831865.0,
            "gross_to_date": 282193031.0,
            "rank": 1,
            "theaters": 2771,
            "theatre_change": 4,
            "week": {
                "$date": 885513600000
            },
            "week_number": 6,
            "week_over_week_change": -0.23
'''




CREATE_MOVIEDB_TBL = '''CREATE TABLE moviesdb (
    movie_id   PRIMARY KEY,
    title      numeric NOT NULL DEFAULT "None",

);'''


# gender: M : Male, Female: F, Not assigned: N
create_actor_tbl = '''CREATE TABLE actors (
  actor_id  serial PRIMARY KEY,
  name      text NOT NULL,
  gender    char(1) NOT NULL DEFAULT 'N'
);'''

create_movie_actor_tbl = ''' CREATE TABLE movies_actors (
  movie_id   int REFERENCES movies (movie_id),
  actor_id   int REFERENCES actors (actor_id),
  CONSTRAINT movie_actor_pkey PRIMARY KEY (movie_id, actor_id)
);
'''


create_director_tbl = '''CREATE TABLE actors (
  actor_id  serial PRIMARY KEY,
  name      text NOT NULL,
  gender    char(1) NOT NULL DEFAULT 'N'
); '''


CREATE_plot_TBL = '''CREATE TABLE movies_plot (
    movie_id   PRIMARY KEY,
    plot        text NOT NULL DEFAULT "plot"
);'''

'''

class _Const(object):
    @constant
    def INSERT():
        return INSERT_IN_MOVIEDB
