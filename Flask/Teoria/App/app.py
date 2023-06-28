
from flask import render_template
app=Flask(__name__)

from flask import Flask
from config import *
app = Flask(__name__,instance_relative_config=True)

@app.route("/about")
def learn():
    return "Flask for web developers!"

app.config.from_object('config')
app.config.from_pyfile('config.py')
@app.route('/')
def index():
    return '<h1>Hello, World! Cubisssssss</h1>'
# app.add_url_rule('/','index',index)
@app.route('/user/<name>')
def user(name):
    return f'<h1>hello, {name}</h1>'
@app.route('/user/<name>')
def user1(name):
    return f'<h1>Bye, {name}!</h1>'