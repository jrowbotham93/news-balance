from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object("src.config.Config")
db = SQLAlchemy(app)


@app.route('/')
def index():
    return 'Index Page'


@app.route('/homepage')
def hello():
    return 'Hello, World'


if __name__ == '__main__':
    app.run(debug=True, port=5500)
