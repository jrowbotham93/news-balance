from flask.cli import FlaskGroup
from src import app, db
from src.models.article import Article
from src.models.publisher import Publisher


cli = FlaskGroup(app)
# docker-compose exec web python manage.py create_db
# docker-compose exec db psql --username=db --dbname=db
@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()
    print("tables created")

# docker-compose exec web python manage.py drop_db
@cli.command("drop_db")
def drop_db():
    db.drop_all()
    db.session.commit()
    print("tables dropped")

# docker-compose exec web python manage.py seed_db
@cli.command("seed_db")
def seed_db():
    db.session.add(Publisher(name="BBC World News"))
    db.session.commit()
    print("seeding database")


if __name__ == "__main__":
    cli()
