from flask import render_template, request
from dbmodels import Person
from flask_login import login_user, logout_user, current_user, login_required
from dbmodels import User

def register_routes(app, db, bcrypt):

    @app.route('/', methods=['GET', 'POST'])
    def index():
        if request.method == 'GET':
            people = Person.query.all()
            return render_template('dbindex.html', people=people)
        elif request.method == 'POST':
            name = request.form.get('name')
            age  = request.form.get('age')
            job  = request.form.get('job')

            person = Person(name=name, age=age, job=job)

            db.session.add(person)
            db.session.commit()

            people = Person.query.all()
            return render_template('dbindex.html', people=people)
        
    @app.route('/delete/<pid>', methods=['DELETE'])
    def delete(pid):
        Person.query.filter(Person.pid == pid).delete()
        db.session.commit()

        people = Person.query.all()
        return render_template('dbindex.html', people=people)
    
    @app.route('/details/<pid>')
    def details(pid):
        person = Person.query.filter(Person.pid==pid).first()
        return render_template('dbdetails.html', person=person)
        

    @app.route('/user', methods=['GET', 'POST'])
    def userindex():
        if current_user.is_authenticated:
            return str(current_user.username)
        else:
            return "No user is logged in..."
        
    @app.route('/signup', methods=['GET', 'POST'])
    def signup():
        if request.method == 'GET':
            return render_template('signup.html')
        elif request.method == 'POST':
            pass

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'GET':
            return render_template('login.html')
        elif request.method == 'POST':
            pass
    
    @app.route('/login/<uid>')
    def login(uid):
        user = User.query.get(uid)
        login_user(user)
        return 'Success'
    
    
    @app.route('/logout')
    def logout():
        logout_user()
        return 'Success'