#!/usr/bin/python
"""Module accesing psql database and modifying it."""
import psycopg2
import sql_stmt


class MovieDB():
    """Class for psql operations."""

    def __init__(self, config):
    """ Initialization method.

     Args:
         config: desc.

     Returns:
         return_value: desc.

     """
        # read database, user, password, host etc from the config file
        try:
            self.conn = psycopg2.connect(database=config['database'],
                                         user=config['user'],
                                         password=config['password'],
                                         host=config['host'],
                                         port=config['port'])
        except:
            print "I am unable to connect to the database"


# __del__ instead
    def close_connection(self):
        self.conn.close()


    def execute_command(self, command):
        cur = self.conn.cursor()
        self.cur.execute(command)
        print "SUCCESS"
        self.conn.commit()
        cur.close()

    def query_command(self, query):
        cur = self.conn.cursor()
        self.cur.execute(query)
        rows = self.cur.fetchall()
        self.query_results(rows)
        self.conn.commit()
        cur.close()

    def query_results(rows):
        for row in rows:
            print row

def insert_into_table(self, insert_stmt, insert_values_l):
    try:
        cur = self.conn.cursor()
        # execute the INSERT statement
        cur.executemany(insert_stmt, vendor_list)
        # commit the changes to the database
        self.conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

#INSERT_IN_MOVIEDB
    def insert_attr_command(self, movie_id, dict_attr):
        cur = self.conn.cursor()
        for attribute, values in dict_attr.items():
            self.cur.execute(sql_stmt.INSERT_IN_MOVIEDB, (movie_id, attribute, values))
            print "Inserted"
        self.conn.commit()
        cur.close()

    def insert_command(self, movie_title):
        cur = self.conn.cursor()
        for attribute, values in dict_attr.items():
            self.cur.execute(sql_stmt.INSERT_IN_MOVIEDB, (attribute, values))
            print "Inserted"
        self.conn.commit()
        cur.close()
