from flask import Flask, request
import operations as op

app = Flask(__name__)

@app.route('/')
def home_page():
    return 'Welcome to my calculator app!'

@app.route('/add')
def add_page():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(op.add(a, b))
    
@app.route('/sub')
def sub_page():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(op.sub(a, b))

@app.route('/mult')
def mult_page():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(op.mult(a, b))

@app.route('/div')
def div_page():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(op.div(a, b))
