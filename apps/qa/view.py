
from flask import (
    Blueprint,
    render_template,
    g,
    request,
    redirect,
    url_for
    )

from sqlalchemy import text, or_  # == order_by(-column)

from middleware.request_decorator import request_login
from .model import QuestionModel, AnswerModel
from EXT.tools import db
from .forms import QuestionForm, AnswerForm

qa_bp = Blueprint("qa", __name__, url_prefix="/qa")


@qa_bp.route("/", methods=["GET", "POST"])
def index():
    questions = QuestionModel.query.order_by(text('-create_time')).all()
    return render_template("index.html", questions=questions)


@qa_bp.route("/question/public", methods=["GET", "POST"])
@request_login
def question_public():
    # print(f"-----------------question methods is {request.method}---------------")
    if request.method == "GET":
        return render_template("question_public.html")
    else:
        form = QuestionForm(request.form)
        if form.validate():
            title = form.title.data
            content = form.content.data

            # save to database
            # print(title, content, g.user, "-----------------------------")
            question = QuestionModel(title=title, content=content, author=g.user)
            db.session.add(question)
            db.session.commit()

            # redirect
            return redirect(url_for("qa.index"))
        else:
            return redirect(url_for("qa.question_public"))


@qa_bp.route("/question/<int:question_id>")
def question_detail(question_id):
    question = QuestionModel.query.get(question_id)
    # answers = AnswerModel.query.filter(question_id=question_id, author=g.user)
    return render_template("question_detail.html", question=question)


@qa_bp.route("/answer/<int:question_id>", methods=["POST"])
def answer(question_id):
    form = AnswerForm(request.form)
    if form.validate():
        # save to mysql
        answer = AnswerModel(content=form.content.data, author=g.user, question_id=question_id)
        db.session.add(answer)
        db.session.commit()

        return redirect(url_for("qa.question_detail", question_id=question_id))

    return redirect(url_for("qa.question_detail", question_id=question_id))


@qa_bp.route("/search")
def search():
    param = request.args.get("q")
    questions = QuestionModel.query.filter(or_(QuestionModel.title.contains(param), QuestionModel.content.contains(param))).order_by(text("-create_time"))
    return render_template("index.html", questions=questions)

