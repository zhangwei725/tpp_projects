from flask_restful import Resource, reqparse, fields, marshal_with

from apps.cinemas.models import Cinemas

# 参数传递
# /list/<int:page>/<int:size>
# ?page=1&size=10


# cinemas?city='武汉'

# 参数一  city  城市   默认 北京
# 参数二


#

'''
1>restful  参数的基本使用
parser.add_argument(arguments,type=None,help='',default=)
# arguments  参数的key 
# type   要转化的参数的类型   
help   参数出现错误时的提示信息    
default  参数的默认值
'''

"""
必要参数 
required=True

"""

# 列表 一个键对应多个值  列表
# 位置参数  form 表单 heads   cookies files(文件上传)  args


# parser.add_argument('name', type=int, action='append')
# parser.add_argument('name', type=int, action='append',location='files')

cinema_fields = {
    'cid': fields.Integer,
    'name': fields.String,
    'city': fields.String,
    'district': fields.String,
    'address': fields.String,
    'phone': fields.String,
    'score': fields.Float,
    'hallnum': fields.Integer,
    'servicecharge': fields.Float,
    'astrict': fields.Integer,
    'flag': fields.Integer,
    'isdelete': fields.Integer,
}

districts_fields = {
    'cid': fields.Integer,
    'district': fields.String,
}

data = {
    'districts': fields.List(fields.Nested(districts_fields)),
    'cinemas': fields.List(fields.Nested(cinema_fields))
}

result = {
    'msg': fields.String(default='success'),
    'status': fields.Integer(default=200),
    'data': fields.Nested(data),
}

"""
合理的合并请求  
1.缓存 一般数据固定

"""


class CinemasResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('city', type=str, default='深圳', required=True, help='必要参数')
        self.parser.add_argument('page', type=int, default=1, )
        self.parser.add_argument('size', type=int, default=10, )
        self.parser.add_argument('district', type=str)
        self.parser.add_argument('keyword', type=str)
        # 1表示升序 0 降序
        self.parser.add_argument('score_sort', type=int)

    @marshal_with(result)
    def get(self):
        # 获取所有参数 返回一个字典对象
        args = self.parser.parse_args()
        # 获取城市参数
        city = args.get('city')
        # 获取区域参数
        district = args.get('district')
        # 获取关键字
        keyword = args.get('keyword')
        # 评分排序字段
        score_sort = args.get('score_sort')
        # 如果参数传了
        query = Cinemas.query.filter(Cinemas.city == city)
        # 判断区域
        if district:
            query = query.filter(Cinemas.district == district)
        # 通过关键字查询
        if keyword:
            query = query.filter(Cinemas.name.like('%{}%'.format(keyword)))
        #  如果用户选择按评分进行排序
        if score_sort:
            if score_sort == 1:
                # 降序  从大到小
                query = query.order_by(Cinemas.score.desc())
            else:
                # 升序  从小到大
                query = query.order_by(Cinemas.score.asc())
        cinemas = query.all()
        # 查询区域
        districts = Cinemas.query.filter(Cinemas.city == city).group_by(Cinemas.district).all()
        data = {
            'districts': districts,
            'cinemas': cinemas
        }
        result = {
            'data': data
        }
        return result


class CinemasDistrict(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('city', type=str, default='深圳', required=True, help='必要参数')
        self.parser.add_argument('district', type=str)

    @marshal_with(result)
    def get(self):
        # 获取所有参数 返回一个字典对象
        args = self.parser.parse_args()
        # 获取城市参数
        city = args.get('city')
        # 获取区域参数
        district = args.get('district')
        # 如果参数传了
        query = Cinemas.query.filter(Cinemas.city == city)
        # 判断区域
        if district:
            query = query.filter(Cinemas.district == district)
        # 查询区域
        districts = Cinemas.query.filter(Cinemas.city == city).group_by(Cinemas.district).all()
        data = {
            'districts': districts,
        }
        result = {
            'data': data
        }
        return result
