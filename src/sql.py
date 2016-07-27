#!/usr/bin/python
import psycopg2
import sql_stmt


class MovieDB():
    def __init__(self):
        # read database, user, password, host etc from the config file
        try:
            self.conn = psycopg2.connect(database="testdb", user="postgres",
                                     password="pass123", host="0.0.0.1",
                                     port="5432")
        except:
            print "I am unable to connect to the database"


# __del__ instead
    def close_connection(self):
        self.conn.close()


    def execute_command(self, command):
        cur = self.conn.cursor()
        self.cur.execute(command)
        print "Table created successfully"
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
