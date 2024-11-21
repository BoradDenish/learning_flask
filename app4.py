from flask import Flask, render_template, request, session, make_response, flash

app = Flask(__name__, template_folder='templates')
app.secret_key = 'SOME KEY'

@app.route('/')
def index():
    return render_template('app4.html', message="Index")

@app.route('/set_data')
def set_data():
    session['name'] = 'Denish'
    session['other'] = 'Hello World!'
    return render_template('app4.html', message='Session data set...')

@app.route('/get_data')
def get_data():
    if 'name' in session.keys() and 'other' in session.keys():
        name = session['name']
        other = session['other']
        return render_template('app4.html', message=f"Name: { name }, Other: { other }")
    else:
        return render_template('app4.html', message=f"No Session Found..")

@app.route('/clear_session')
def clear_session():
    session.clear()
    return render_template('app4.html', message="Clear session data...")

@app.route('/set_cookie')
def set_cookie():
    response = make_response(
        render_template('app4.html', message='Cookie set...!')
    )
    response.set_cookie('cookie_name', 'Denish....')
    return response

@app.route('/get_cookie')
def get_cookie():
    if 'cookie_name' in request.cookies.keys():
        cookie_value = request.cookies['cookie_name']
        return render_template('app4.html', message=f'Cookie Value: {cookie_value}')
    else:
        return render_template('app4.html', message=f'Cookie value not found...!!')

@app.route('/remove_cookie')
def remove_cookie():
    response = make_response(
        render_template('app4.html', message='Cookie removed...!')
    )
    response.set_cookie('cookie_name', expires=5)
    return response

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form.get('username') 
        password = request.form.get('password') 
        if username == "denish" and password == 'pass':
            flash('Successful Login!')
            return render_template('app4.html', message="")
        else:
            flash('Login Failed!')
            return render_template('app4.html', message="")

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)