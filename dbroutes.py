from flask import redirect, render_template, request, url_for
from dbmodels import Person
from flask_login import login_user, logout_user, current_user, login_required
from dbmodels import User

def register_routes(app, db, bcrypt):
    # Default Flask Authentication

    # @app.route('/', methods=['GET', 'POST'])
    # def index():
    #     if request.method == 'GET':
    #         people = Person.query.all()
    #         return render_template('dbindex.html', people=people)
    #     elif request.method == 'POST':
    #         name = request.form.get('name')
    #         age  = request.form.get('age')
    #         job  = request.form.get('job')

    #         person = Person(name=name, age=age, job=job)

    #         db.session.add(person)
    #         db.session.commit()

    #         people = Person.query.all()
    #         return render_template('dbindex.html', people=people)
        
    # @app.route('/delete/<pid>', methods=['DELETE'])
    # def delete(pid):
    #     Person.query.filter(Person.pid == pid).delete()
    #     db.session.commit()

    #     people = Person.query.all()
    #     return render_template('dbindex.html', people=people)
    
    # @app.route('/details/<pid>')
    # def details(pid):
    #     person = Person.query.filter(Person.pid==pid).first()
    #     return render_template('dbdetails.html', person=person)
        

    # Custome Authentication
    @app.route('/', methods=['GET', 'POST'])
    def userindex():
        return render_template('userindex.html')
        # if current_user.is_authenticated:
            # return str(current_user.username)
        # else:
        #     return "No user is logged in..."


    @app.route('/signup', methods=['GET', 'POST'])
    def signup():
        if request.method == 'GET':
            return render_template('signup.html')
        elif request.method == 'POST':
            username = request.form.get('username')
            password = request.form.get('password')
            hashed_password = bcrypt.generate_password_hash(password)
            user = User(username=username, password=hashed_password)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('userindex'))


    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'GET':
            return render_template('login.html')
        elif request.method == 'POST':
            username = request.form.get('username')
            password = request.form.get('password')

            user = User.query.filter(User.username == username).first()
            print("Hello!!22@@", user.password)

            if bcrypt.check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for('userindex'))
            else:
                return 'Failed!'

  
    # @app.route('/login/<uid>')
    # def login(uid):
    #     user = User.query.get(uid)
    #     login_user(user)
    #     return 'Success'
    
    
    @app.route('/logout')
    def logout():
        logout_user()
        # return 'Success'
        return redirect(url_for('userindex'))


    @app.route('/secret')
    @login_required
    def secret():
        return 'My Secret Message.....!!'

