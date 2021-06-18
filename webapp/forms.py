from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo

class LoginForm(FlaskForm):
    username = StringField('Имя пользователя:', validators=[DataRequired()], render_kw={"class": "form-control"})
    password = PasswordField('Пароль:', validators=[DataRequired()], render_kw={"class": "form-control"})
    submit = SubmitField('Отправить!', render_kw={"class": "btn btn-primary"})

class RegisterForm(FlaskForm):
    username = StringField("Имя пользователя:", validators=[DataRequired()], id="username", render_kw={"class": "form-control"})
    password = PasswordField("Пароль:", validators=[DataRequired()], id="password", render_kw={"class": "form-control"})
    confirmpassword = PasswordField("Подтвердите пароль:", validators=[DataRequired(), EqualTo('password', message="Passwords don't match")], id="conpassword", render_kw={"class": "form-control"})
    submit = SubmitField('Отправить!', render_kw={"class": "btn btn-primary"})
  


