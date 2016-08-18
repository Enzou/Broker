import logging

from flask import request
from flask_restplus import Resource
from api.restplus import api, ma

from database import db
from database.models import Shop


log = logging.getLogger(__name__)

ns = api.namespace('shops', description="Operations related to shops")


class ShopSchema(ma.ModelSchema):
    class Meta:
        model = Shop
        fields = ('sid', 'name', 'address', 'zip', 'city')


shop_schema = ShopSchema()


@ns.route('')
@ns.route('/')
class ShopList(Resource):

    def get(self):
        """Fetch a list of all available shops"""
        shops = Shop.query.all()
        return shop_schema.dump(shops, many=True).data


    @api.response(201, 'Shop successfully added')
    def post(self):
        """Create a new shop"""
        shop = shop_schema.load(request.json)

        db.session.add(shop.data)
        db.session.commit()

        return None, 201



@ns.route('/<int:id>')
class ShopRes(Resource):

    def get(self, id):
        """Fetch a shop with the given id"""
        shop = Shop.query.filter_by(sid=id).first()
        return shop_schema.dump(shop).data


    @api.response(204, 'Shop sucessfully updated')
    def put(self, id):
        """Update the shop with the given id"""
        s = Shop.query.filter_by(sid=id).first()
        shop = shop_schema.load(request.json, instance=s)     # directly update the object from the db

        db.session.commit()

        return None, 204


    @api.response(204, 'Shop successfully deleted')
    def delete(self, id):
        """Delete the shop with the given id"""
        s = Shop.query.filter_by(sid=id).first()

        db.session.delete(s)
        db.session.commit()

        return None, 204

