# encoding utf-8

class Config(object):
    @staticmethod
    def init_app(app):
        pass

class DBConfig(Config):
    user = 'root'
    passwd = 'root'
    db = 'sober'
    host = 'localhost'
    charset = 'utf8'

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}