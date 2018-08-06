from apps.ext import db


class Cinemas(db.Model):
    cid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), unique=True, nullable=False, index=True)

