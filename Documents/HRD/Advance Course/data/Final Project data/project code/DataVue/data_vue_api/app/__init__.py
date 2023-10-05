from flask import Flask

from .resources.resource import ns
from flask_restx import Api



def create_app():

    app = Flask(__name__)
    # app.debug = True
    api = Api(app, version='1.0', title='DataVue', description='api including scraping, create model')

    api.add_namespace(ns)
    return app