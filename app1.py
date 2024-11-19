from flask import Flask, redirect, render_template, url_for

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    params1 = "Hello"
    params2 = "World !"
    mylist = ['Apple', 'Orange', 'Banana', 'Mango']
    return render_template('index.html', params1 = params1, params2 = params2, mylist = mylist)


@app.route('/other')
def other():
    some_text = "Hello World !!"
    return render_template('other.html', some_text=some_text)


@app.template_filter('reverse_string')
def reverse_string(s):
    return s[::-1]


@app.template_filter('repeat')
def repeat(s, times=2):
    return s * times

@app.template_filter('alternate_case')
def alternate_case(s):
    return "".join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(s)])

@app.route('/redirect_endpoint')
def redirect_endpoint():
    return redirect(url_for('other'))


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)