import logging
import sys

from flask import request, jsonify
from flask_restplus import Resource
from api.restplus import api, ma

from database import db
from database.models import Person


log = logging.getLogger(__name__)

ns = api.namespace('persons', description="Operations related to persons")


class PersonSchema(ma.ModelSchema):
    class Meta:
        model = Person
        fields = ('pid', 'firstname', 'lastname', 'username', 'email', 'iban', 'bic')


person_schema = PersonSchema()


@ns.route('')
@ns.route('/')
class PersonList(Resource):

    def get(self):
        """Fetch a list of all available persons"""
        persons = Person.query.all()
        return person_schema.dump(persons, many=True).data


    @api.response(201, 'Person successfully added')
    def post(self):
        """Create a new person"""
        pers = person_schema.load(request.json)

        db.session.add(pers.data)
        db.session.commit()

        print('Person: ' + str(type(pers)), file=sys.stderr)

        return pers.data, 201



@ns.route('/<int:id>')
class PersonRes(Resource):

    def get(self, id):
        """Fetch a person with the given id"""
        person = Person.query.filter_by(pid=id).first()
        return person_schema.dump(person).data


    @api.response(204, 'Person sucessfully updated')
    def put(self, id):
        """Update the person with the given id"""
        p = Person.query.filter_by(pid=id).first()
        pers = person_schema.load(request.json, instance=p)     # directly update the object from the db

        db.session.commit()

        return None, 204


    @api.response(204, 'Person successfully deleted')
    def delete(self, id):
        """Delete the person with the given id"""
        p = Person.query.filter_by(pid=id).first()

        db.session.delete(p)
        db.session.commit()

        return None, 204


@ns.route('/<string:username>')
class PersonRes(Resource):

    def get(self, username):
        """Fetch a person with the given id"""
        person = Person.query.filter_by(username=username).first()
        return person_schema.dump(person).data


    @api.response(204, 'Person sucessfully updated')
    def put(self, username):
        """Update the person with the given id"""
        p = Person.query.filter_by(username=username).first()
        pers = person_schema.load(request.json, instance=p)     # directly update the object from the db

        db.session.commit()

        return None, 204


    @api.response(204, 'Person successfully deleted')
    def delete(self, username):
        """Delete the person with the given id"""
        p = Person.query.filter_by(username=username).first()

        db.session.delete(p)
        db.session.commit()

        return None, 204
