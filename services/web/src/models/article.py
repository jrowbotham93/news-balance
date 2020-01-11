from src import db


class Article(db.Model):
    __tablename__ = "Article"

    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(128))
    title = db.Column(db.String(128), default=True, nullable=False)
    abstract = db.Column(db.String(1000), unique=True, nullable=False)
    content = db.Column(db.String(100000), nullable=False)
    urlToImage = db.Column(db.String(128))
    publishedAt = db.Column(db.DateTime)

    publisher = db.Column(db.Integer, db.ForeignKey('Publisher.id'))
    source = db.relationship("Publisher")

    def __init__(self):
        pass

    def __repr__(self):
        return f'<Article model {self.id}>'
