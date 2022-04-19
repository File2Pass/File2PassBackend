import os

DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = os.getenv("FILE2PASS_USERNAME")
PASSWORD = os.getenv("FILE2PASS_PASSWORD")
HOST = os.getenv("FILE2PASS_HOST")
PORT = 3306
DATABASE = os.getenv("FILE2PASS_DBNAME")


class Config:
    SECRET_KEY = os.getenv("FILE2PASS_SECRET_KEY")
    SESSION_TYPE = 'filesystem'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = \
        "{}+{}://{}:{}@{}:{}/{}?charset=utf8mb4".format(
            DIALECT,
            DRIVER,
            USERNAME,
            PASSWORD,
            HOST,
            PORT,
            DATABASE
        )


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = \
        "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(
            DIALECT,
            DRIVER,
            USERNAME,
            PASSWORD,
            HOST,
            PORT,
            DATABASE
        )


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = \
        "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(
            DIALECT,
            DRIVER,
            USERNAME,
            PASSWORD,
            HOST,
            PORT,
            DATABASE
        )

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)


config = {
    'developments': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
