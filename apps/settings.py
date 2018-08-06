# 通过类的方式去配置flask项目的配置文件


def get_db_uri(db_config):
    engine = db_config.get('ENGINE') or 'mysql'
    driver = db_config.get('DRIVER') or 'pymysql'
    user = db_config.get('USER') or 'root'
    password = db_config.get('PASSWORD') or 'root'
    host = db_config.get('HOST') or '127.0.0.1'
    port = db_config.get('PORT') or '3306'
    db_name = db_config.get('DB_NAME')
    return '{}+{}://{}:{}@{}:{}/{}'.format(engine, driver, user, password, host, port, db_name)


class Config:
    DEBUG = False
    # 登录的对密码,对session数据加密的秘钥
    SECRET_KEY = '110'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(Config):
    DEBUG = True
    DATABASE = {
        #
        # 'ENGINE': 'mysql',
        # 'DRIVER': 'pymysql',
        # 数据库用户名
        # 'USER': 'root',
        # 'PASSWORD': 'root',
        # 'HOST': '127,0,0,1',
        # 'PORT': '3306',
        'DB_NAME': 'tpp1',
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


class ProductConfig(Config):
    DATABASE = {
        'ENGINE': 'mysql',
        'DRIVER': 'pymysql',
        # 数据库用户名
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '47.106.89.6',
        'PORT': '3306',
        'DB_NAME': 'tpp',
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)
