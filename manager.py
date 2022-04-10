

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
# from apps import create_app
from EXT.tools import db
from EXT import create_app

from apps.user.model import EmailCaptcha
from apps.qa import QuestionModel

app = create_app()

manager = Manager(app=app)

Migrate(app=app, db=db)

manager.add_command("db", MigrateCommand)


if __name__ == '__main__':
    # app.run()
    manager.run()
