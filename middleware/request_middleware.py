from flask import session, g  # 全局变量，flask独有属性

from EXT import create_app
from apps.user.model import UserModel

app = create_app()


@app.before_request
def defore_request():
    user_id = session.get("user_id")
    if user_id:
        try:
            user = UserModel.query.get(user_id)
            g.user = user
        except:
            g.user = None


@app.context_processor
def context_processor():
    if hasattr(g, "user"):
        return {"user": g.user}
    else:
        return {}

