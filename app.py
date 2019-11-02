from flask import Flask, render_template
from forms import CadastrarUsuario

app = Flask(__name__)

@app.route('/inicio')
def index():
    return render_template('index.html')

@app.route('/cadastrar', methods = ['GET', 'POST'])
def cadastrar():
    form = CadastrarUsuario()

    return render_template('register.html', form = form)

if __name__ == ('__main__'):
    app.run(debug=True)