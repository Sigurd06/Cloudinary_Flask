import logging
from os import getenv
from flask import Flask
from flask_cors import CORS
from settings import settings

def create_app(settings_name):
    app = Flask(__name__)
    app.config.from_object(settings[settings_name])
    settings[settings_name].init_app(app)

    CORS(app)
    
    logging.basicConfig(level=logging.DEBUG)
    app.logger.info("CLOUD_NAME :: %s", getenv('CLOUD_NAME'))

    @app.route('/')
    def index():
        return 'Hello World'

    from .upload import upload_bp
    app.register_blueprint(upload_bp)

    return app