from src import db


class Publisher(db.Model):
    __tablename__ = "Publisher"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), default=True, nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'<Publisher model {self.id}>'
