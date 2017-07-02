from flask import Flask, render_template
from flask import request
from flask.ext.bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

bootstrap = Bootstrap(app)

app.config.from_object('config')
db = SQLAlchemy(app)
#import models

@app.route('/')
def hello_world():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s</p>' % user_agent

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello,%s!</h1>' % name

@app.route('/hello')
def hello():
    return render_template('hello.html')

if __name__ == '__main__':
    app.run()
