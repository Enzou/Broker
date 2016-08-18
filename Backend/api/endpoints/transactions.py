import logging
import sys

from flask import request, make_response, jsonify
from flask_restplus import Resource, fields
from api.restplus import api, ma

from database import db
from database.models import Transaction, Asset


log = logging.getLogger(__name__)

ns = api.namespace('transactions', description="Operations related to transactions")

class AssetSchema(ma.ModelSchema):
    aid = fields.Integer(dump_only=True)
    class Meta:
        model = Asset
        fields = ('aid', 'trans_id', 'title', 'amount', 'debitor_id', 'comment', 'tag', 'quantity')


class TransactionSchema(ma.ModelSchema):
    tid = fields.Integer(dump_only=True)
    assets = fields.Nested(AssetSchema, many=True)

    class Meta:
        model = Transaction
        fields = ('tid', 'creditor_id', 'shop_id', 'date', 'comment', 'assets')
    


transaction_schema = TransactionSchema()
asset_schema = AssetSchema()



@ns.route('')
@ns.route('/')
class TransactionList(Resource):

    def get(self):
        """Fetch a list of all available transactions"""
        transactions = Transaction.query.all()
        return transaction_schema.dump(transactions, many=True).data


    @api.response(201, 'Transaction successfully added')
    def post(self):
        """Create a new transaction"""
        txn, errors = transaction_schema.load(request.json, session=db.session)

        if errors:
            db.rollback()
            print('Transaction had errors: ' + errors)
            return make_response(jsonify({'error': 101, 'message': str(errors)}), 403)

        db.session.add(txn)
        db.session.commit()

        return transaction_schema.dump(txn).data, 201



@ns.route('/<int:id>')
class TransactionRes(Resource):

    def get(self, id):
        """Fetch a transaction with the given id"""
        transaction = Transaction.query.filter_by(tid=id).first()
        return transaction_schema.dump(transaction).data


    @api.response(204, 'Transaction sucessfully updated')
    def put(self, id):
        """Update the transaction with the given id"""
        txn = Transaction.query.filter_by(tid=id).first()
        txn = transaction_schema.load(request.json, instance=txn)     # directly update the object from the db

        db.session.commit()

        return None, 204


    @api.response(204, 'Transaction successfully deleted')
    def delete(self, id):
        """Delete the transaction with the given id"""
        txn = Transaction.query.filter_by(tid=id).first()

        db.session.delete(txn)
        db.session.commit()

        return None, 204

