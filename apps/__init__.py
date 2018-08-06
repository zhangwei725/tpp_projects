from flask import Flask

app = Flask(__name__)

app.debug = True


def create_app():
        
    return app
