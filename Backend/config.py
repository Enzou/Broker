import os
basedir = os.path.abspath(os.path.dirname(__file__))

FLASK_DEBUG = True

SQLALCHEMY_TRACK_MODIFICATIONS = False      # disable warning
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
#SQLALCHEMY_DATABASE_URI = 'mysql://root@localhost/broker'
#SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

