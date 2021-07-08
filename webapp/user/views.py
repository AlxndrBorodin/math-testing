from flask import Blueprint, flash, render_template, redirect, url_for
from flask_login import current_user, login_user, logout_user

from webapp.user.forms import LoginForm
from webapp.user.models import User, Teacher_students, Test

blueprint = Blueprint('user', __name__, url_prefix='/users')

@blueprint.route('/login')
def login():
    if current_user.is_authenticated:
        return redirection(url_for('index'))
    title = "Авторизация"
    login_form = LoginForm()
    return render_template('login.html', page_title=title, form=login_form)

@blueprint.route('/process-login', methods=['POST'])
def process_login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            flash('Вы вошли на сайт')
            return redirect(url_for('index'))

    flash('Неправильное имя пользователя или пароль')
    return redirect(url_for('user.login'))

@blueprint.route('/logout')
def logout():
    logout_user()
    flash('Вы успешно разлогинились')
    return redirect(url_for('index'))

@blueprint.route('/register')
def register():
    title = "Регистрация"
    reg_form = RegisterForm()
    return render_template("register.html", page_title=title, form=reg_form)

@blueprint.route('/start-test')
def start_test():
    title = 'Начать тестирование'
    if current_user.is_authenticated:
       def get_teacher_student(current_user):
            student_belongs = User.query.filter(User.name == name, User.id == student_id).first()
            student_list = []
            if not student_belongs:
                teacher_students = Teacher_students(student_id=User.id, teacher_id=Test.id_teacher)
                db_session.add(student_list)
                db_session.commit()
            return student_list
