import datetime

from apps.ext import db


class Movies(db.Model):
    __tablename__ = 'movies'
    mid = db.Column(db.Integer, primary_key=True)
    id = db.Column(db.Integer)
    showname = db.Column(db.String(64), unique=True, nullable=False, index=True)
    shownameen = db.Column(db.String(64), nullable=False, index=True)
    director = db.Column(db.String(64))
    leadingRole = db.Column(db.String(64))
    type = db.Column(db.String(64))
    country = db.Column(db.String(64))
    language = db.Column(db.String(64))
    duration = db.Column(db.Integer)
    screeningmodel = db.Column(db.String(10))
    openday = db.Column(db.DateTime, default=datetime.datetime.now())
    backgroundpicture = db.Column(db.String(64))
    flag = db.Column(db.Integer, default=1)
    isdelete = db.Column(db.Boolean, default=False)

# class Movies(db.Model):
#     __tablename__ = 'movies'
#     mid = db.Column(db.Integer, primary_key=True)
#     # 影片的中文名称
#     name = db.Column(db.String(64), unique=True, nullable=False, index=True)
#     # 英文的名称
#     shownameen = db.Column(db.String(64), nullable=False, index=True)
#     # 导演
#     director = db.Column(db.String(64))
#     # 主演
#     leading_role = db.Column(db.String(64))
#     # 类型
#     type = db.Column(db.String(64))
#     # 国家
#     country = db.Column(db.String(64))
#     # 语言
#     language = db.Column(db.String(64))
#     # 放映时长
#     duration = db.Column(db.Integer)
#     # 放映模式
#     screening_model = db.Column(db.String(10))
#     #  上映的时间
#     openday = db.Column(db.DateTime, default=datetime.datetime.now())
#     #  影片背景图
#     bg_pic = db.Column(db.String(64))
#     # 状态   True 表示热映   false 即将上映
#     flag = db.Column(db.Boolean, default=True)
#     # 是否删除
#     is_delete = db.Column(db.Boolean, default=False)
