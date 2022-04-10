
import string, random, datetime

from flask import Blueprint, render_template, request, redirect, url_for, jsonify, session, flash
from werkzeug.security import generate_password_hash, check_password_hash

from flask_mail import Message


from EXT.tools import mail, db
from apps.user.model import EmailCaptcha, UserModel
from .forms import RegisterForm, LoginForm

bp_user = Blueprint("user", __name__, url_prefix="/user")


@bp_user.route("/", methods=["GET", "POST"])
def login():
    # TODO login 逻辑处理，存放此处
    if request.method == "POST":
        form = LoginForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            user = UserModel.query.filter_by(email=email).first()
            if user and check_password_hash(user.password, password):
                session["user_id"] = user.id
                # setattr(session, "user_id", user.id)
                return redirect(url_for("qa.index"))
            else:
                flash("用户名或密码错误，请重新输入")
                return render_template("login.html")
        else:
            flash("用户名或密码错误，请重新输入")
            return render_template("login.html")

    else:
        return render_template("login.html")


@bp_user.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("user.login"))


@bp_user.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        forms = RegisterForm(request.form)
        # print("##"*20 + f"\n forms post data is :{forms} \n" + "##"*30)
        if forms.validate():
            # print("##" * 20 + "\n forms post data is validate ... \n" + "##" * 30)
            # 验证通过
            username = forms.username.data
            email = forms.email.data
            password = forms.password.data
            # password = "12345678"
            hash_password = generate_password_hash(password)  # 密码加密
            print("##" * 20 + f"\n generate password {hash_password} ... \n" + "##" * 30)
            user_modle = UserModel(username=username, email=email, password=hash_password)
            db.session.add(user_modle)
            db.session.commit()
            return redirect(url_for("user.login"))
        else:
            # print("##" * 20 + "\n form信息没有验证通过，GG ... \n" + "##" * 30)
            return redirect(url_for("user.register"))
    else:
        # print("##" * 20 + "\n form信息没有验证通过，GG ... \n" + "##" * 30)
        return render_template("register.html")


# @bp_user.route("/mail")
# def send_mail():
#     message = Message(
#         subject='这个是测试邮件',
#         recipients=["2522096401@qq.com"],
#         body="你好啊，傻蛋")
#     mail.send(message)
#     return "success"


@bp_user.route("/captcha", methods=["POST",])
def get_captcha():
    # methods = request.method
    email = request.form["email"]
    # email = request.args.get("email")
    captcha_param = string.ascii_letters + string.digits
    captcha_data = random.sample(captcha_param, 4)
    captcha_msg = "".join(captcha_data)
    if email:
        try:
            message = Message(
                subject='验证码 邮件',
                recipients=[f"{email}"],
                body=f"{captcha_msg}")
            mail.send(message)
        except Exception as e:
            # print(f"fail to send email to user, err msg : {e}")
            return jsonify({"code": 400, "message": "请先确认邮件是否可用"})
        # 保存数据库

        email_model = EmailCaptcha.query.filter_by(email=email).first()
        if email_model:
            # email_model.email = email
            email_model.captcha = captcha_msg
            email_model.latest_time = datetime.datetime.now()
            db.session.commit()
        else:
            email_model = EmailCaptcha(email=email, captcha=captcha_msg, latest_time=datetime.datetime.now())
            db.session.add(email_model)
            db.session.commit()
        return jsonify({"code": 200})
    else:
        return jsonify({"code": 400, "message": "请先确认邮件"})

