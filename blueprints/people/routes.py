from flask import request, render_template, redirect, url_for, Blueprint

from blueprints.blueprintapp import db
from blueprints.people.models import People

people = Blueprint('people', __name__, template_folder='templates')

@people.route('/')
def index():
    people = People.query.all()
    return render_template('people/index.html', people=people)


@people.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('people/create.html')
    elif request.method == 'POST':
        name    = request.form.get('name')
        age     = int(request.form.get('age'))
        job     = request.form.get('job')

        job = job if job != "" else None

        people = People(name=name, age=age, job=job)

        db.session.add(people)
        db.session.commit()

        return redirect(url_for('people.index'))