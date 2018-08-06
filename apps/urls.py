from flask_restful import Api

from apps.main.apis import MainResource

api = Api()
# url('', ''.name)
api.add_resource(MainResource, '/', endpoint='main')


def init_api(app):
    api.init_app(app)
