from flask_restful import Resource, fields, marshal_with

# {
#     'msg': 'success',
#     'status': 200,
#     'data': {
#           'banners':[]
#            'hots':[]
#            'nows':[]

# }
# }
from apps.movies.models import Movies

banner_fields = {
    'id': fields.Integer,
    'url': fields.String
}

movie_fields = {
    'showname': fields.String,
    'shownameen': fields.String,
    'director': fields.String,
    'leading_role': fields.String,
    'type': fields.String,
    'country': fields.String,
    'language': fields.String,
    'duration': fields.String,
    'screening_model': fields.String,
    'backgroundpicture': fields.String,
    'openday': fields.DateTime,
}

data = {
    'hots': fields.List(fields.Nested(movie_fields)),
    'nows': fields.List(fields.Nested(movie_fields)),
    'hot_count': fields.Integer,
    'now_count': fields.Integer,
}

result = {
    'msg': fields.String(default='success'),
    'status': fields.Integer(default=200),
    'data': fields.Nested(data),
}


# 8000
class IndexApi(Resource):
    @marshal_with(result)
    def get(self):
        #    limit  1    6
        # select *  from movies  where  flag= 1  limit 1 offset 5
        # 热映数据
        # Movies.query.filter(Movies.flag == True).order_by('mid').paginate(page=1, per_page=5).items
        hot_movies = Movies.query.filter(Movies.flag == 1).limit(5).all()
        now_movies = Movies.query.filter(Movies.flag == 2).limit(5).all()
        # 查询热映总条数
        hot_count = Movies.query.filter(Movies.flag == 1).count()
        now_count = Movies.query.filter(Movies.flag == 2).count()
        data = {
            'hots': hot_movies,
            'nows': now_movies,
            'hot_count': hot_count,
            'now_count': now_count,
        }
        result = {
            'data': data
        }
        return result
