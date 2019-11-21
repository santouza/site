from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from forms import CadastroUsuario, Doacoes

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///CSD.db'
app.config['SECRET_KEY'] = 'ajlkecbgajlkecbg' 

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80), unique = True, nullable = True)
    email = db.Column(db.String(12), nullable = False)
    password = db.Column(db.String(120), unique = True, nullable = False)

    def __repr__(self):
        return '<User %r>' % self.username

class Doar(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    n_pecas = db.Column(db.Integer)
    d_pecas = db.Column(db.String(150), nullable = False)

    def __repr__(self):
        return '<Doar %r>' % self.n_pecas

db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastrar', methods = ['GET', 'POST'])
def cadastrar():
    form = CadastroUsuario()
    if form.validate_on_submit ():
        user = User()
        user.username = form.username.data
        user.email = form.email.data
        user.password = form.password.data
        db.session.add(user)
        db.session.commit()

    return render_template('register.html', form = form)

@app.route('/doar')
def doacoes():
    form = Doacoes()
    return render_template('doacoes.html', form = form)

if __name__ == ('__main__'):
    app.run(debug=True)