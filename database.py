"""_summary_

Returns:
    _type_: _description_
"""
import os
import urllib.parse
import psycopg

from dotenv import dotenv_values
from tqdm import tqdm

os.chdir(os.path.dirname(__file__))

if os.path.exists(".env"):
    config = dotenv_values(".env")
else:
    config = dotenv_values("default.env")


FILENAME_DB_SHEMA = "database/database.sql"
options = urllib.parse.quote_plus("--search_path=modern,public")
CONN_PARAMS = f"postgresql://{config['USER']}:{config['PASSWORD']}@{config['HOST']}:{config['PORT']}/{config['DATABASE']}?options={options}"  # pylint: disable=line-too-long


def reset_table():  # pylint: disable=missing-function-docstring
    with psycopg.connect(CONN_PARAMS) as conn:  # pylint: disable=not-context-manager
        with conn.cursor() as cur:
            with open(FILENAME_DB_SHEMA, "r", encoding="utf-8") as file:
                cur.execute(file.read())


def get_data():  # pylint: disable=missing-function-docstring
    with psycopg.connect(CONN_PARAMS) as conn:  # pylint: disable=not-context-manager
        with conn.cursor() as cur:
            cur.execute("select * from data;")
            return cur.fetchall()
