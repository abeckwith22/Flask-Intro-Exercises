## My submission for 23.1 Flask Intro Exercises

`greet/app.py`
```python
# Put your app in here.
from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def welcome():
    return 'welcome'

@app.route('/welcome/home')
def welcome_home():
    return 'welcome home!'

@app.route('/welcome/back')
def welcome_back():
    return 'welcome back!'
```

`calc/app.py`
```python
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

```