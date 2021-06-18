from flask import Flask, render_template

from webapp.forms import LoginForm, RegisterForm

app = Flask(__name__)

@app.route('/')
def index():
    title = "Математические тесты"
    return render_template('index.html', page_title=title)

@app.route('/login')
def login():
    title = "Авторизация"
    login_form = LoginForm()
    return render_template('login.html', page_title=title, form=login_form)

@app.route('/register', methods=["POST"])
def register():
    title = "Регистрация"
    reg_form = RegisterForm()
    return render_template("register.html", page_title=title, form=reg_form)

if __name__ == "__main__":
    app.run(debug=True)