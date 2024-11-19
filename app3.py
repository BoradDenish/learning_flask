from flask import Flask, redirect, render_template, url_for

app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path="/")

@app.route('/')
def index():
    return render_template('app3.html')

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)