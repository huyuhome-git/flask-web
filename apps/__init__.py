
from flask import Flask
from apps.user import bp_user
from apps.qa import qa_bp
from settings import *
import pymysql

def create_app():
    app = Flask(__name__, template_folder="../templates", static_folder="../static")

    # settings
    app.config.from_object(DevelopmentConfig)

    app.register_blueprint(bp_user)
    app.register_blueprint(qa_bp)

    return app
