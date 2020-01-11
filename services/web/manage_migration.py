from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from src import app, db
from src.models.article import Article
from src.models.publisher import Publisher

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()

# docker-compose exec web python manage.py db init
# docker-compose exec web python manage.py db migrate
# docker-compose exec web python manage.py db upgrade
# docker-compose exec web python manage.py db upgrade --sql > migration.sql
