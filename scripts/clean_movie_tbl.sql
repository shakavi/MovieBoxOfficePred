-- Filename: clean_movie_tbl.sql
--
-- Script for cleaning tables(deleting all data) for MovieBoxOfficePred. 
--

--
-- Name: movies; Type: TABLE; Schema: public; Owner: shakavi;
--
DELETE FROM movies;


--
-- Name: moviesattr; Type: TABLE; Schema: public; Owner: shakavi;
--
DELETE FROM moviesattr;


--
-- Name: movies; Type: TABLE; Schema: public; Owner: shakavi;
--
DELETE FROM box_office_col;
