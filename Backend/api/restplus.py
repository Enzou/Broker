import logging
import config as CONFIG

from flask_restplus import Api

log = logging.getLogger(__name__)


api = Api(version='1.0', title='Broker API',
        description='A simple API for handling transactions')


@api.errorhandler
def default_error_handler(e):
    message = 'An unhandled exception occcured'
    log.exception(message)

    if not CONFIG.FLASK_DEBUG:
        return {'message': messag}, 500
