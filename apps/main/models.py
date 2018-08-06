from apps.ext import db


class Banner(db.Model):
    url = db.Column(db.String(255), nullable=True)
