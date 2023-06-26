import os
from flask import Flask, jsonify, render_template
from database import reset_table, get_data, get_img, get_video, get_music

os.chdir(os.path.dirname(__file__))


app = Flask(__name__)


@app.route("/")
def index():  # pylint: disable=missing-function-docstring
    return render_template("index.html")


@app.route("/getDatabase", methods=["GET"])
def get_database():  # pylint: disable=missing-function-docstring
    return jsonify(get_data())


@app.route("/getImg", methods=["GET"])
def get_img_route():  # pylint: disable=missing-function-docstring
    title, img_data, type = get_img()
    res = {"title": title, "img_data": img_data, "type": type}
    return res


@app.route("/getVideo", methods=["GET"])
def get_video_route():  # pylint: disable=missing-function-docstring
    title, video_data, type = get_video()
    res = {"title": title, "video_data": video_data, "type": type}
    return res


@app.route("/getMusic", methods=["GET"])
def get_music_route():  # pylint: disable=missing-function-docstring
    title, music_data, type = get_music()
    res = {"title": title, "music_data": music_data, "type": type}
    return res


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
