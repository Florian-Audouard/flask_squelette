import os
from flask import Flask, jsonify, render_template
from database import reset_table, get_data, get_img

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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
