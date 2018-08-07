from apps.ext import db


# 影厅
class Cinemas(db.Model):
    cid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), unique=True, nullable=False, index=True)
    city = db.Column(db.String(64))
    area = db.Column(db.String(64))
    detail = db.Column(db.String(255))
    bg_pic = db.Column(db.String(100))
    # True 开发     false 关闭
    status = db.Column(db.Boolean, default=True)
    tel = db.Column(db.String(11))
    # 是否删除
    is_active = db.Column(db.Boolean, default=True)


# 影厅
class Halls(db.Model):
    hid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    # 1表示 2D 21 3D 3表示4D  4 表示  3D MAX
    screen_type = db.Column(db.Integer, nullable=False)
    seat_num = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Boolean, default=True)
    is_active = db.Column(db.Boolean, default=True)
    cid = db.Column(db.Integer, db.ForeignKey(Cinemas.cid))


"""
座位 seat
seat_id

座位类型
x
y
状态(损坏,正常)
是否删除


影厅id
影院id
"""


class Seats(db.Model):
    sid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 1.普通  2.豪华 3 超豪华
    type = db.Column(db.Integer, nullable=False)
    x = db.Column(db.Integer, nullable=False)
    y = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Boolean, default=True)
    is_active = db.Column(db.Boolean, default=True)
    # 是否可选
    is_choose = db.Column(db.Boolean, default=True)
    #     外键设置
    cid = db.Column(db.Integer, db.ForeignKey(Cinemas.cid))
    hid = db.Column(db.Integer, db.ForeignKey(Halls.hid))
