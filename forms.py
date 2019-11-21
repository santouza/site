#coding: utf-8
from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, SubmitField, BooleanField, TextAreaField)
from wtforms.validators import DataRequired, Length, Email, EqualTo

class CadastroUsuario(FlaskForm):
    username = StringField('Usuário', validators = [DataRequired(), Length(min = 2, max = 80)])
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Senha', validators = [DataRequired()])
    conf_password = PasswordField('Confirme sua senha', validators = [DataRequired(), EqualTo('password')])
    submit = SubmitField('Cadastrar')

class Doacoes(FlaskForm):
    n_pecas = StringField('Nº de peças', validators = [DataRequired()])
    d_pecas = TextAreaField('Descrição das peças', validators = [DataRequired()])
    botao = SubmitField('Doar')