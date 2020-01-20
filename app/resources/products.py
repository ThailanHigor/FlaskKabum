from flask_restful import Resource, marshal
from app import request
from app.schemas import product_fields
from app.services.kabumService import KabumService
from flask.views import MethodView


class Products(MethodView):
    service =  KabumService()

    def get(self, id): 
        product = self.service.getProduct(id)
        return marshal(product, product_fields, 'product')
    
    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass

