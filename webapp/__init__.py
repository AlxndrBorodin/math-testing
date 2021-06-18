from flask import Flask, render_template

from webapp.forms import LoginForm, RegisterForm
#from webapp.model import db

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    #db.init_app(app)

    @app.route('/')
    def index():
        title = "Главная страница"
        return render_template('index.html', page_title=title)

    @app.route('/login')
    def login():
        title = "Авторизация"
        login_form = LoginForm()
        return render_template('login.html', page_title=title, form=login_form)

    @app.route('/register')
    def register():
        title = "Регистрация"
        reg_form = RegisterForm()
        return render_template("register.html", page_title=title, form=reg_form)

    return app