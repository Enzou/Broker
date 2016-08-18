import config as CONFIG

from flask import Flask, Blueprint
from database import db
from api.restplus import api, ma
from api.endpoints.persons import ns as persons_ns
from api.endpoints.shops import ns as shops_ns
from api.endpoints.transactions import ns as transactions_ns


app = Flask(__name__)


def init_api(flask_app):
    ma.init_app(flask_app)
    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)
    api.add_namespace(persons_ns)
    api.add_namespace(shops_ns)
    api.add_namespace(transactions_ns)
    flask_app.register_blueprint(blueprint)


def init_app(flask_app):
    app.config.from_object('config')
    db.init_app(flask_app)


def main():
    init_app(app)
    init_api(app)
    app.run(host='0.0.0.0', debug=CONFIG.FLASK_DEBUG)


if __name__ == '__main__':
    main()


