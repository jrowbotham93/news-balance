from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object("src.config.Config")
db = SQLAlchemy(app)


class Articles(db.Model):
    __tablename__ = "Articles"

    id = db.Column(db.Integer, primary_key=True)
    publisher = db.Column(db.String(128), default=True, nullable=False)
    article = db.Column(db.String(128), unique=True, nullable=False)

    def __init__(self):
        pass

@app.route('/')
def index():
    return 'Index Page'


@app.route('/homepage')
def hello():
    return 'Hello, World'


if __name__ == '__main__':
    app.run(debug=True, port=5500)
