from flask import Flask
from flask_restful import Api

from config import config

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    api = Api(app)

    from app.resources.products import Products

    app.add_url_rule("/product/<int:id>", view_func=Products.as_view("product"), methods = ["GET"])

    return app
