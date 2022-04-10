
import pymysql
from apps import create_app
from EXT.tools import db, mail

app = create_app()


def create_app():
    db.init_app(app)  # db
    mail.init_app(app)

    return app
