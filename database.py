"""_summary_

Returns:
    _type_: _description_
"""
import os
import urllib.parse
import psycopg
import base64
from dotenv import dotenv_values

os.chdir(os.path.dirname(__file__))

default_look_filename = ".env"

if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and (sys.argv[0] == "--site" or sys.argv[1] == "--site"):
        default_look_filename = "site.env"

if os.path.exists(default_look_filename):
    config = dotenv_values(default_look_filename)
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
            cur.execute("select img_title,img_data,img_type from img_data;")
            img_title, img_data, img_type = cur.fetchall()[0]
            img_data = img_data.decode("utf-8")
            return (img_title, img_data, img_type)


def get_video():  # pylint: disable=missing-function-docstring
    with psycopg.connect(CONN_PARAMS) as conn:  # pylint: disable=not-context-manager
        with conn.cursor() as cur:
            cur.execute("select video_title,video_data,video_type from video_data;")
            video_title, video_data, video_type = cur.fetchall()[0]
            video_data = video_data.decode("utf-8")
            return (video_title, video_data, video_type)


def get_music():  # pylint: disable=missing-function-docstring
    with psycopg.connect(CONN_PARAMS) as conn:  # pylint: disable=not-context-manager
        with conn.cursor() as cur:
            cur.execute("select music_title,music_data,music_type from music_data;")
            music_title, music_data, music_type = cur.fetchall()[0]
            music_data = music_data.decode("utf-8")
            return (music_title, music_data, music_type)


def add_img(title, data, type):
    with psycopg.connect(CONN_PARAMS) as conn:  # pylint: disable=not-context-manager
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO img_data (img_title,img_data,img_type) VALUES (%(title)s,%(byte)s,%(type)s)",
                {"title": title, "byte": data, "type": type},
            )


def add_music(title, data, type):
    with psycopg.connect(CONN_PARAMS) as conn:  # pylint: disable=not-context-manager
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO music_data (music_title,music_data,music_type) VALUES (%(title)s,%(byte)s,%(type)s)",
                {"title": title, "byte": data, "type": type},
            )


def add_video(title, data, type):
    with psycopg.connect(CONN_PARAMS) as conn:  # pylint: disable=not-context-manager
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO video_data (video_title,video_data,video_type) VALUES (%(title)s,%(byte)s,%(type)s)",
                {"title": title, "byte": data, "type": type},
            )


if __name__ == "__main__":
    reset_table()
    with psycopg.connect(CONN_PARAMS) as conn:  # pylint: disable=not-context-manager
        with conn.cursor() as cur:
            # Insert an image into the table
            with open("media/voiture.jpg", "rb") as f:
                image_data = base64.b64encode(f.read())
                add_img("voiture", image_data, "jpg")
            with open("media/Rick_Roll.mp4", "rb") as f:
                video_data = base64.b64encode(f.read())
                add_video("RickRoll", video_data, "mp4")
            with open("media/music.mp3", "rb") as f:
                video_data = base64.b64encode(f.read())
                add_music("music", video_data, "mp3")
