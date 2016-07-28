-- Filename: create_movie_db.sql
--
-- Script for creating tables for MovieBoxOfficePred
--


--
-- Name: movies; Type: TABLE; Schema: public; Owner: shakavi;
--

CREATE TABLE IF NOT EXISTS movies(
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
);


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
    average_per_theatre numeric NOT NULL DEFAULT 0,
    gross               numeric NOT NULL DEFAULT 0,
    rank                numeric NOT NULL DEFAULT 0,
    theaters            numeric NOT NULL DEFAULT 0,
    date_of_week        date,
    week_over_week_change numeric NOT NULL DEFAULT 0,
    CONSTRAINT box_office_pkey PRIMARY KEY (movie_id, week_number)
);
