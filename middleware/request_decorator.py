
from flask import g, redirect, url_for

from functools import wraps



def request_login(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if hasattr(g, "user"):
            return func(*args, **kwargs)
        else:
            return redirect(url_for("user.login"))

    return wrapper

