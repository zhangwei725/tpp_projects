from flask_caching import Cache
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy


def init_ext(app):
    init_db(app)
    init_cache(app)
    init_cors(app)


"""
===========数据库配置 start==========

"""

db = SQLAlchemy()
from flask_migrate import Migrate

migrate = Migrate()


def init_db(app):
    db.init_app(app)
    migrate.init_app(app, db)


"""
========缓存配置=========
"""

cache = Cache()


def init_cache(app):
    cache_config = {
        'CACHE_TYPE': 'redis',
        'CACHE_DEFAULT_TIMEOUT': 60,
        'CACHE_REDIS_HOST': '47.106.89.6',
        'CACHE_REDIS_PORT': '6379',
        # 'CACHE_REDIS_PASSWORD': '',
        'CACHE__REDIS_DB': 8
    }
    cache.init_app(app, cache_config)


"""
========跨域请求配置=========
"""
cors = CORS()


# v3
# api/v2/    前端  移动端
# 老版本


def init_cors(app):
    # 针对所有的访问
    # cors.init_app(app, supports_credentials=True)
    # 针对部分接口提供跨域请求
    cors.init_app(app, resources={'/api/*': {'orgins': '*'}})
