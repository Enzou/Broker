from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import app, init_app     # import the variables from the actual app, otherwise migrate won't work
from database import db

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

import database.models           # add all relevant tables


if __name__ == '__main__':
    init_app(app)
    manager.run()

# commands:

# 1) python db_migrate.py db init           initialize migrations
# 2) python db_migrate.py db migrate        identify changes and create version script
# 3) python db_migrate.py db upgrade        push changes to the database
