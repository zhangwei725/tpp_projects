from flask_restful import Api

from apps.cinemas.apis import CinemasResource, CinemasDistrict, CinemasDetail
from apps.main.apis import IndexApi

from apps.movies.apis import MoviesListApi

api = Api(prefix='/api/v1')

'''==== 首页相关 start ===='''
api.add_resource(IndexApi, '/', '/index/')
'''==== 首页相关 end ===='''

'''==== 影院相关 start ===='''
api.add_resource(CinemasResource, '/cinemas/list/')
api.add_resource(CinemasDistrict, '/cinemas/dist/')
api.add_resource(CinemasDetail, '/cinemas/detail/')
'''==== 影院相关 end ===='''

'''==== 影片相关 start ===='''
api.add_resource(MoviesListApi, '/movies/list/<int:page>/<int:size>/')

'''==== 影片相关 end ===='''


def init_api(app):
    api.init_app(app)
