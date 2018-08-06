from flask_restful import Api

api = Api()


# url('', ''.name)


def init_api(app):
    api.init_app(app)
