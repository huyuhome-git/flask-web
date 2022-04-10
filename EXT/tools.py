
from flask_sqlalchemy import SQLAlchemy  # sql
from flask_mail import Mail

"""
# 注意事项:
如果有相互调用的python包模块，比如apps EXT
需要将相互调用的方法，属性抽取出来，单独存放，还需要是独立的属性，没有其他管理，或调用其他模块
这样就可以解耦
"""

db = SQLAlchemy()  # db
mail = Mail()  # mail
