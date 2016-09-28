from flask import Flask, render_template, redirect, url_for, request
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
manager = Manager(app)
db = SQLAlchemy(app)

class Orden(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    orden = db.Column(db.Integer)
    fecha = db.Column(db.DateTime)

    def __init__(self, orden, fecha):
        self.orden = orden
        self.fecha = fecha

    def __repr__(self):
        return '<orden %r>' % self.orden


@app.route('/')
def index():
    return ('funcionando')

@app.route('/login', methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Credenciales incorrectas, Intantalo de nuevo'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)


if __name__ == '__main__':
    manager.run()
