
import wtforms
from wtforms.validators import length, email, EqualTo

from .model import EmailCaptcha, UserModel


class RegisterForm(wtforms.Form):  # wtforms.Form class
    username = wtforms.StringField(validators=[length(min=3, max=20)])
    email = wtforms.StringField(validators=[email()])
    password = wtforms.StringField(validators=[length(min=6, max=20)])
    password_confirm = wtforms.StringField(validators=[EqualTo("password")])

    def validate_captcha(self, field):
        # 验证captcha字段
        # print("##" * 20 + "\n validate captcha .... \n" + "##" * 30)
        captcha = field.data
        email = self.email.data
        captcha_modle = EmailCaptcha.query.filter_by(email=email).first()
        if not (captcha_modle and captcha_modle.email.lower() == captcha.lower()):
            # print("##" * 20 + "\n fail validate captcha .... \n" + "##" * 30)
            raise wtforms.ValidationError("验证captcha字段失败")
        # print("##" * 20 + "\n end validate captcha .... \n" + "##" * 30)

    def validate_email(self, field):
        # print("##" * 20 + "\n validate email .... \n" + "##" * 30)
        email = field.data
        user_modle = UserModel.query.filter_by(email=email).first()
        # print("##" * 20 + f"\n validate email : {user_modle}.... \n" + "##" * 30)
        if user_modle:
            # print("##" * 20 + "\n fail validate email .... \n" + "##" * 30)
            raise wtforms.ValidationError("邮箱已经注册")
        # print("##" * 20 + "\n end validate emil .... \n" + "##" * 30)


class LoginForm(wtforms.Form):  # wtforms.Form class
    email = wtforms.StringField(validators=[length(min=6, max=20)])
    password = wtforms.StringField(validators=[length(min=6, max=20)])

