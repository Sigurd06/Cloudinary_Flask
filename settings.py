import os

class Config(object):
    SECRET_KEY = 'secret'
    
    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    ENV = 'development'
    DEBUG = True
    CLOUD_NAME = os.getenv('CLOUD_NAME')
    API_KEY = os.getenv('CLOUD_API_KEY')
    API_SECRET = os.getenv('CLOUD_API_SECRET')

settings = {
    'development': DevelopmentConfig,

    'default': DevelopmentConfig
}
