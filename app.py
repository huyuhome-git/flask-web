from flask import session, g

from EXT import create_app
from middleware import request_middleware
from apps.user.model import UserModel
from apps.qa import QuestionModel

app = create_app()


if __name__ == '__main__':
    app.run()
