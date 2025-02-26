import os
from flask import Flask, g
from . import db

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.before_request
    def load_logged_in_user():
        g.user = {'id': 1, 'username': 'user_ex'}

    db.init_app(app)

    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    @app.route('/hello')
    def hello():
        return 'Hello, this is our lab!'

    return app
