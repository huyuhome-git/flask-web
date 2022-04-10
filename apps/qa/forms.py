
import wtforms
from wtforms.validators import length


class QuestionForm(wtforms.Form):  # wtforms.Form class
    title = wtforms.StringField(validators=[length(min=3, max=50)])
    content = wtforms.StringField(validators=[length(min=5)])


class AnswerForm(wtforms.Form):
    content = wtforms.StringField(validators=[length(min=1)])
