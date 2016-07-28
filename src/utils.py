"""Module containing helper functions."""
import ConfigParser
# import io
from itertools import islice

def get_data_dict(data):
    """Method: Cleanup data and convert it in the dict format."""
    data_s = data.to_json()  # string
    data_d = json.loads(data_s)  # dict
    return data_d

def take(n, iterable):
    """Return first n items of the iterable as a list."""
    return list(islice(iterable, n))


'''
key: to obtain the value to be inserted in the sql database
value:  is the column name in the sql table

'''
# comment
mojo_movie_tbl_d = {'title': 'title',
                    'release_date': 'release_date',
                    'runtime': 'runtimes',
                    'mpaa_rating': 'mpaa',
                    'production_budget': 'Budget'}

# comment
imdb_movie_tbl_d = {'languages': 'languages',
                    'plot': 'plot',
                    'rating': 'rating',
                    'countries': 'country'}


def get_data_for_movie_db(movie_data_d, src_movie_data_d, src_movie_tbl_d):
    """get data in a dictonary which is to be inputin the psql db."""
    for key, value in src_movie_tbl_d.items():
        if (key == 'runtime' or key == 'production_budget'):
            movie_data_d[value] = int(src_movie_data_d[key])
        elif (key == 'countries' or key == 'languages'):
            movie_data_d[value] = src_movie_data_d[key][0]
        else:
            movie_data_d[value] = src_movie_data_d[key]
    return movie_data_d


def read_config(filename, section):
    """read the config file data for the given section.

    Args:
        filename: the config file name.
        section: the section of the config file which  is to be read.

    Returns:
        section_info(dict): dictionary containing the options and
            value under the given section.

    """
    # section = "db_config"
    # "../config/config.ini"
    section_info = {}

    # initilize the config parser
    config = ConfigParser.ConfigParser()
    # read the file
    config.read(filename)
    # get all the options associated with the section
    options = config.options(section)
    for option in options:
        try:
            section_info[option] = config.get(section, option)
            if section_info[option] == -1:
                # DebugPrint("skip: %s" % option)
                print("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            section_info[option] = None
    print section_info
    return section_info
