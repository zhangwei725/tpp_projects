import datetime
from decimal import Decimal

from flask_restful import Resource, fields, marshal_with

# {
#     status:
#       msg:''
#       data{
#             pager:{
#                 'total':100
#                  'size' :10
#                  'page_count':

#             }
#             movies:[
#                   {},
#                   {}
#
# ]
#
# }
#
# }
# ?page=1&size=10
#
# page  per_page
# 必要参数  page   size
from apps.movies.models import Movies

pager = {
    'total': fields.Integer,
    'pages': fields.Integer,
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
    # 分页数据
    'pager': fields.Nested(pager),
    # 热映
    'hots': fields.List(fields.Nested(movie_fields)),
    # 即将上映
    'upcomings': fields.List(fields.Nested(movie_fields)),
}

result = {
    'msg': fields.String(default='success'),
    'status': fields.Integer(default=200),
    'data': fields.Nested(data),
}


# 因为都是基本类型
class MoviesListApi(Resource):
    @marshal_with(result)
    def get(self, page, size):
        try:
            paginate1 = Movies.query.filter(Movies.flag == 1).paginate(page=page, per_page=size, error_out=False)
            paginate2 = Movies.query.filter(Movies.flag == 2).paginate(page=page, per_page=size, error_out=False)
            data = {
                #  paginate1.total   总记录数
                # paginate.pages     总页数
                'pager': {'total': paginate1.total, 'pages': paginate1.pages},
                'hots': paginate1.items,
                'upcomings': paginate2.items
            }

            result = {
                'data': data
            }
        except:
            result = {
                'status': 404,
                'msg': 'error'
            }
        return result

# 字典
# 列表
# 基本类型 字符窜  数字类型  Boolean   None

# 拿到所有keys
# 就能拿到所有的值
# 判断值的类型
# 如果是特殊的数据类型需要转换成基本类型  ,
# 保存到字典中
# page_dict = to_dict(paginate1)
# def to_dict(obj):
#     objs = {}
#     # datetime   decimal
#     # vars(obj).keys()
#     # vars(objs).values()
#     if obj:
#         for key in vars(obj).keys():
#             value = getattr(obj, key)
#             if isinstance(value, datetime.datetime):
#                 value = datetime.datetime.strftime('%Y-%m-%d %H-%M-%S')
#             elif isinstance(value, datetime.date):
#                 value = datetime.datetime.strftime('%Y-%m-%d')
#             elif isinstance(value, Decimal):
#                 value = str(Decimal(value).quantize(Decimal('0.00')))
#             objs[key] = value
#     return objs
