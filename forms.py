from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, PasswordField, DateField, RadioField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Email
from flask_wtf.file import FileField, FileAllowed

class AddPostForm(FlaskForm):
    title = StringField("პოსტის სათაური", validators=[DataRequired()])
    desc = TextAreaField("დაწერეთ რამე", validators=[DataRequired()])
    img = FileField('გინდათ სურათის ატვირთვა?', validators=[FileAllowed(['jpg', 'png'], 'Images only!')])

    Submit = SubmitField('დაპოსტვა')


class RegisterForm(FlaskForm):
  name = StringField('სახელი')
  surname = StringField('გვარი')
  email = StringField('მეილი')
  password = PasswordField('პაროლი')
  repeat_password = PasswordField('გაიმეორეთ პაროლი')
  repeat_password = PasswordField('გაიმეორეთ პაროლი')
  gender = RadioField('მონიშნეთ სქესი', choices=['მამრობითი', 'მდედრობითი'])
  date = DateField('დაბადების თარიღი')
  country  = SelectField('მონიშნეთ ქვეყანა', choices=["საქართველო", "აშშ", "საფრანგეთი", "დიდი ბრიტანეთი"])

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')