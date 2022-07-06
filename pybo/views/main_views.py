from flask import Blueprint
from flask import Blueprint, render_template

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/hellodeepblue')
def hello_pybo():
    return render_template('question/test.html')


@bp.route('/')
def index():
    return render_template('question/question_list.html')