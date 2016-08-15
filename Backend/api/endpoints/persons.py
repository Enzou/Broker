import logging

from flask import request
from flask_restplus import Resource
from api.restplus import api
from api.serializers import person_schema

from database import db
from database.models import Person


log = logging.getLogger(__name__)


ns = api.namespace('persons', description="General api")


# apiPfx = '/api/'


@ns.route('')
@ns.route('/')
class PersonList(Resource):

    @api.marshal_list_with(person_schema)
    def get(self):                              # return all persons
        persons = Person.query.all()
        return persons


    @api.expect(person_schema)
    @api.response(201, 'Person successfully added')
    def post(self):                             # add a person
        data = request.json
        
        firstname = data.get('firstname')
        lastname = data.get('lastname')
        username = data.get('username')
        email = data.get('email')
        pwd = data.get('pwd')
        iban = data.get('iban')
        bic = data.get('bic')

        pers = Person(firstname, lastname, username, email=email, pwd=pwd, iban=iban, bic=bic)

        db.session.add(pers)
        db.session.commit()

        return None, 201



@ns.route('/<int:id>')
class PersonRes(Resource):

    @api.marshal_with(person_schema)
    def get(self, id):                          # return a person
        person = Person.query.filter_by(pid=id).first()
        return person


    @api.expect(person_schema)
    @api.response(204, 'Person sucessfully updated')
    def put(self, id):                          # update a person
        data = request.json
        p = Person.query.filter_by(pid=id).first()

        p.firstname = data.get('firstname')
        p.lastname = data.get('lastname')
        p.username = data.get('username')
        p.email = data.get('email')
        p.pwd = data.get('pwd')
        p.iban = data.get('iban')
        p.bic = data.get('bic')

        db.session.commit()

        return None, 204


    @api.response(204, 'Person successfully deleted')
    def delete(self, id):                       # delete a person
        p = Person.query.get(id).first()

        db.session.delete(p)
        db.session.commit()

        return None, 204

