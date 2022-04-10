import pymysql


class Config:
    DEBUG = True

    # connect mysql
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:mysql@127.0.0.1:3306/project_demo2?charset=utf8"

    # sql
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = True

    # email
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    # 注意此处，很多人配置发不出去和这个是有关系的
    MAIL_PASSWORD = 'nlgzapbfmsafdjgc'
    MAIL_USERNAME = '2522096401@qq.com'
    MAIL_DEFAULT_SENDER = "2522096401@qq.com"

    # session secret_key
    SECRET_KEY = 'big big dream'


class DevelopmentConfig(Config):
    EVN = "development"


class ProductionConfig(Config):
    ENV = "product"
    DEBUG = False

