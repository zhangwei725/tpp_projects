from flask_restful import Api

from apps.main.apis import IndexApi

# http://xxx//api/v1/idnex/

api = Api(prefix='/api/v1')

# url('', ''.name)
api.add_resource(IndexApi, '/', '/index/')


def init_api(app):
    api.init_app(app)
