from flask import Flask, redirect, render_template, url_for, request

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'GET':
        return render_template('app2.html')

    elif request.method == 'POST':

        username = request.form.get('username')
        password = request.form.get('password')

        if username =="denish" and password == 'pass':
            return "Success"
        else:
            return "Failed"

@app.route('/file_upload', methods=['POST'])
def file_upload():
    file = request.files['file']
    
    if file.content_type == 'text/plain':
        return file.read().decode()
    elif file.content_type == '':
        return ""
        # df = pd.read_excel(file)
        # return df.to_html()
        

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)