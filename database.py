"""_summary_

Returns:
    _type_: _description_
"""
import os
import urllib.parse
import psycopg
import base64
from dotenv import dotenv_values
import sys

os.chdir(os.path.dirname(__file__))
if sys.argv[1] == "--site" or sys.argv[0] == "--site":
    config = dotenv_values("site.env")
elif os.path.exists(".env"):
    config = dotenv_values(".env")
else:
    config = {
        "USER": os.environ.get("USER_DB"),
        "PASSWORD": os.environ.get("PASSWORD_DB"),
        "HOST": os.environ.get("HOST_DB"),
        "PORT": os.environ.get("PORT_DB"),
        "DATABASE": os.environ.get("DATABASE_DB"),
    }

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


def get_img():  # pylint: disable=missing-function-docstring
    with psycopg.connect(CONN_PARAMS) as conn:  # pylint: disable=not-context-manager
        with conn.cursor() as cur:
            cur.execute("select title,img_data from img_data;")
            title, img_data = cur.fetchone()
            img_data = img_data.decode("utf-8")
            return (title, img_data)


if __name__ == "__main__":
    reset_table()
    with psycopg.connect(CONN_PARAMS) as conn:  # pylint: disable=not-context-manager
        with conn.cursor() as cur:
            # Insert an image into the table
            image_data = base64.b64encode(open("media/voiture.jpg", "rb").read())
            cur.execute(
                "INSERT INTO img_data (title,img_data) VALUES (%(title)s,%(byte)s)",
                {"title": "voiture", "byte": image_data},
            )
