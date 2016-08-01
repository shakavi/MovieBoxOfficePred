-- Filename: create_movie_db.sql
--
-- Script for creating tables for MovieBoxOfficePred
--


--
-- Name: movies; Type: TABLE; Schema: public; Owner: shakavi;
--

CREATE TABLE IF NOT EXISTS movies(
    movie_id   serial NOT NULL PRIMARY KEY,
    title      text NOT NULL,
    release_date text,
    runtime    numeric,
    language   text,
    country    text,
    budget     numeric,
    rating     numeric,
    mpaa       text,
    plot       text,
    revenue    numeric
);

ALTER TABLE movies ADD UNIQUE (title);

--
-- Name: moviesattr; Type: TABLE; Schema: public; Owner: shakavi;
--

CREATE TABLE  IF NOT EXISTS moviesattr(
    movie_id  int REFERENCES movies (movie_id),
    attr_key  text NOT NULL,
    attr_value text NOT NULL,
    CONSTRAINT movieattr_pkey PRIMARY KEY (movie_id, attr_key, attr_value)
);

--
-- Name: box_office_col; Type: TABLE; Schema: public; Owner: shakavi;
--

CREATE TABLE  IF NOT EXISTS box_office_col(
    movie_id            int REFERENCES movies (movie_id),
    week_number         numeric NOT NULL DEFAULT 0,
    average_per_theatre numeric,
    gross               numeric,
    rank                numeric,
    theaters            numeric,
    date_of_week        text ,
    week_over_week_change numeric,
    CONSTRAINT box_office_pkey PRIMARY KEY (movie_id, week_number)
);
