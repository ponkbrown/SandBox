import os
from flask import Flask, session
from flask import Blueprint
from flask.ext.script import Manager
from sys import version

app = Flask(__name__)
manager = Manager(app)

@app.route('/')
def index():
    return('Hola mundo {}'.format(version))

blue = Blueprint('blueprint', __name__, template_folder='templates')

@blue.route('/')
def show():
    return'Hola BluePrinte!'

app.register_blueprint(blue, url_prefix='/blue')

if __name__ == "__main__":
    manager.run()
