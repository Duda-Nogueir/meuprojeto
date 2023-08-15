from flask_wtf import FlaskForm
from wtforms import StringField,EmailField,TelField,TextAreaField,SubmitField
from wtforms.validators import DataRequired
from flask_wtf.csrf import CSRFProtect


class Contato(FlaskForm):
    nome = StringField('nome', validators=[DataRequired()])
    email = EmailField('email', validators=[DataRequired()])
    telefone = TelField('telefone', validators=[DataRequired()])
    mensagem = TextAreaField('mensagem')
    enviar = SubmitField('enviar')