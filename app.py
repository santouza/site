from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, UserMixin, current_user 
from forms import CadastroUsuario, LoginUsuario, Doacoes

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///CSD.db'
app.config['SECRET_KEY'] = 'ajlkecbgajlkecbg' 

login_manager = LoginManager(app)
db = SQLAlchemy(app)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(12), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    
    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymou(self):
        return False
      
    def get_id(self):
        return str(self.id)

    def __repr__(self):
        return '<User %r>' % self.username

class Doar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    n_pecas = db.Column(db.Integer)
    d_pecas = db.Column(db.String(150), nullable=False)

    def __repr__(self):
        return '<Doar %r>' % self.n_pecas


def __init__(self, username, email, password):
    self.username = username
    self.email = email
    self.password = generate_password_hash(password)

@login_manager.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()

@app.route('/')
def index():
    print(current_user)
    return render_template('index.html')

@app.route('/cadastrar', methods = ['GET', 'POST'])
def cadastrar():
    form = CadastroUsuario()
    if form.validate_on_submit():
        username = form.username.data
        name = form.name.data
        email = form.email.data
        password = form.password.data
        user = User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first()
        if user:
            flash("Insira dados válidos")
            return redirect(url_for('cadastrar'))

        user = User(username=username, name=name, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("login"))
    return render_template('register.html', form = form)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginUsuario()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            flash("Acesso permitido")
            return redirect(url_for("index"))
        else:
            flash("Acesso negado")
    return render_template("login.html", form=form)   

@app.route('/doar', methods = ['GET', 'POST'])
def doacoes():
    form = Doacoes()
    if request.method == 'POST':
        doar = Doar()
        doar.n_pecas = request.form['n_pecas']
        doar.d_pecas = request.form['d_pecas']
        db.session.add(doar)
        db.session.commit()
        flash("Obrigado pela sua doação!")
        return redirect(url_for("index"))

    return render_template('doacoes.html', form = form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/quemsomos')
def quemsomos():

    return render_template('quemsomos.html')

if __name__ == ('__main__'):
    app.run(debug=True)