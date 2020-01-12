import os
from flask_sqlalchemy import SQLAlchemy
from werkzeug import secure_filename
from .apis.api import response_news
from flask import (
    Flask,
    jsonify,
    send_from_directory,
    request,
    redirect,
    url_for
)


app = Flask(__name__)
app.config.from_object("src.config.Config")
db = SQLAlchemy(app)


@app.route('/')
def index():
    return 'Index Page'


@app.route('/homepage')
def hello():
    return response_news.json()


@app.route("/static/<path:filename>")
def staticfiles(filename):
    return send_from_directory(app.config["STATIC_FOLDER"], filename)


@app.route("/media/<path:filename>")
def mediafiles(filename):
    return send_from_directory(app.config["MEDIA_FOLDER"], filename)


@app.route("/upload", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        file = request.files["file"]
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config["MEDIA_FOLDER"], filename))
    return f"""
    <!doctype html>
    <title>upload new File</title>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file><input type=submit value=Upload>
    </form>
    """


if __name__ == '__main__':
    app.run(debug=True, port=5500)
