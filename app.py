from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from forms import CadastroUsuario

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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastrar', methods = ['GET', 'POST'])
def cadastrar():
    form = CadastroUsuario()

    return render_template('register.html', form = form)

@app.route('/', methods = ['GET', 'POST'])
def login():
    form = LoginUsuario()

    return render_template('index.html', form = form)

if __name__ == ('__main__'):
    app.run(debug=True)