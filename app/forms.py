from flask_wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired(message=None)])
    remember_me = BooleanField('remember_me', default=False)

class PostForm(Form):
    title = StringField('Title', validators=[DataRequired(message=None)])
    user_name = StringField('user_name', validators=[DataRequired(message=None)])
    body  = StringField('Body', validators=[DataRequired(message=None)])

