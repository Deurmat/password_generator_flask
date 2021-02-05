from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dsjhnjh2f;lj3of8y 0238[-p'

    from .views import views

    app.register_blueprint(views, url_prefix='/')

    return app
