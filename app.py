from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World"

# using status code 
@app.route('/hello')
def hello():
    return "hello world\n", 202

# Make custom responses
@app.route('/make_response')
def response_make():
    response = make_response('Hello World !!!')
    response.status_code = 404
    # response.headers['content-type'] = 'application/octet-stream'
    response.headers['content-type'] = 'text/plain'
    return response

# How to set methods
@app.route('/methods', methods=['GET', 'POST'])
def methods():
    if request.method == 'GET':
        return "This you made a GET request\n"
    elif request.method == 'POST':
        return "This you made a POST request\n"
    else:
        return "You will never see this message\n"

# How to get params from endpoint
@app.route('/greet/<name>')
def greet(name):
    return f"Hello {name}"

@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    return f"{num1} + {num2} = {num1 + num2}"

@app.route('/handle_url_params')
def heandle_params():
    # return str(request.args)

    if 'num1' in request.args.keys() and 'num2' in request.args.keys():
        # This style get value and if not give value so give error
        num1 = request.args['num1']

        # This Give None if params not have value
        # num1 = request.args.get('num1')
        num2 = request.args.get('num2')
        return f'{num1}, {num2}'
    else:
        return "Some params are missing!!"


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)