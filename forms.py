#coding: utf-8
from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, SubmitField, BooleanField, TextAreaField)
from wtforms.validators import DataRequired, Length, Email

class CadastroUsuario(FlaskForm):
    username = StringField('Usuário', validators = [DataRequired(), Length(min = 2, max = 80)])
    name = StringField('Nome', validators = [DataRequired()])
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Senha', validators = [DataRequired()])
    submit = SubmitField('Cadastrar')

class LoginUsuario(FlaskForm):
    username = StringField('Usuário', validators = [DataRequired()])
    password = PasswordField('Senha', validators = [DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Entrar')

class Doacoes(FlaskForm):
    n_pecas = StringField('Nº de peças', validators = [DataRequired()])
    d_pecas = TextAreaField('Descrição das peças', validators = [DataRequired()])
    botao = SubmitField('Doar')