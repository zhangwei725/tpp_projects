from flask_restful import Resource, reqparse, fields, marshal_with

from apps.cinemas.models import Cinemas, Platoon

# 参数传递
# /list/<int:page>/<int:size>
# ?page=1&size=10


# cinemas?city='武汉'

# 参数一  city  城市   默认 北京
# 参数二


#
from apps.movies.models import Movies

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
movie_fields = {
    'mid': fields.Integer,
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
plat_fields = {
    'pid': fields.Integer,
    'origin_price': fields.Float,
    'discount_price': fields.Float,
    'start_time': fields.DateTime,
    'end_time': fields.DateTime,
}

data = {
    'districts': fields.List(fields.Nested(districts_fields)),
    'cinemas': fields.List(fields.Nested(cinema_fields)),
    'cinema': fields.Nested(cinema_fields),
    'movies': fields.List(fields.Nested(movie_fields)),
    'plats': fields.List(fields.Nested(plat_fields))
}
# 能写代码叫愚公移山   会写代码叫女娲补天    # 10行代码
# 工作经验   工作年限
# 准备两个月
#  唯品会    今日头条   陌陌
#   15k  20k
# 第一年  第二年 进上市公司 21k  14 年薪 + 项目奖金    第三年 bat

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


# 肤浅

#  程序的优化  表的设计
#  关心表之间的关联关系
#  优秀程序员关心数据结构, 差的关心的代码bug
#  查看影院详情


class CinemasDetail(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('cid', type=int, required=True)

    # 1-2   3-4  5年
    @marshal_with(result)
    def get(self):
        cid = self.parser.parse_args().get('cid')
        # 获取当前影院所有的排片信息
        plats = Platoon.query.filter(Platoon.cid == cid).all()
        # 影院的信息
        cinema = Cinemas.query.get(cid)
        # 影片的数据
        movies = []
        for plat in plats:
            movie = Movies.query.get(plat.mid)
            movies.append(movie)
        data = {
            'movies': movies,
            'plats': plats,
            'cinema': cinema,
        }
        result = {
            'data': data
        }
        return result
