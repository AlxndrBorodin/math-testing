from flask import Blueprint, render_template

from webapp.test.models import Test

blueprint = Blueprint('test', __name__)

@blueprint.route('/')
def index():
    title = "Главная страница"
    return render_template('index.html', page_title=title)

@blueprint.route('/test')
def index():
    title = 'Математические тесты'