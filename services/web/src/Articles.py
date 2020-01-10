from . import db


class Articles(db.Model):
    __tablename__ = "Articles"

    id = db.Column(db.Integer, primary_key=True)
    publisher = db.Column(db.String(128), default=True, nullable=False)
    article = db.Column(db.String(128), unique=True, nullable=False)
