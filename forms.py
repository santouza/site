from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, SubmitField, BooleanField)
from wtforms.validators import DataRequired, Length, Email, EqualTo

class CadatroUsuario(FlaskForm):
    username = StringField('Usuário', validators = [DataRequired(), Length(min = 2, mas = 80)])
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Senha', validators = [DataRequired()])
    conf_password = PasswordField('Confirme sua senha', validators = [DataRequired(), EqualTo('password')])
    submit = SumbmitField('Cadastrar')