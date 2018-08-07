from flask_restful import Api

from apps.main.apis import IndexApi

from apps.movies.apis import MoviesListApi

api = Api(prefix='/api/v1')


api.add_resource(IndexApi, '/', '/index/')
api.add_resource(MoviesListApi, '/movies/list/<int:page>/<int:size>/')


def init_api(app):
    api.init_app(app)
