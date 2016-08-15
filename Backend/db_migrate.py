from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import app, db     # import the variables from the actual app, otherwise migrate won't work

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

import app.models           # add all relevant tables


if __name__ == '__main__':
    manager.run()

# commands:

# 1) python db_migrate.py db init           initialize migrations
# 2) python db_migrate.py db migrate        identify changes and create version script
# 3) python db_migrate.py db upgrade        push changes to the database
