from flask_restplus import fields
from api.restplus import api


person_schema = api.model('Person', {
    'pid': fields.Integer(readOnly=True, description='The unique identifier of a person'),
    'firstname': fields.String(readOnly=False, description='The firstname of a person'),
    'lastname': fields.String(readOnly=False, description='The lastname of a person'),
    'username': fields.String(readOnly=False, description='The nickname of a person'),
    'email': fields.String(readOnly=False, description='The email address of a person'),
    'pwd': fields.String(readOnly=False, description='The hash of the password of a person'),
    'iban': fields.String(readOnly=False, description='The IBAN number of a persons bank account'),
    'bic': fields.String(readOnly=False, description='The BIC of a persons bank account')
})

