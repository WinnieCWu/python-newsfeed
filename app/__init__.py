from flask import Flask
from app.routes import home, dashboard
#import home & dashboard modules from routes package


def create_app(test_config=None):
    #set up app test config
    app = Flask(__name__, static_url_path='/')
    app.url_map.strict_slashes = False
    app.config.from_mapping(
        SECRET_KEY='super_secret_key'
    )
    #decorator turns hello() into a route, and the fxn's return becomes the route's response
    @app.route('/hello')
    def hello():
        return 'hello world'
    
    # register routes
    app.register_blueprint(home)
    app.register_blueprint(dashboard)

    return app