from app import app 
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html',titulo = 'Página inicial')



# rota para projetos

@app.route('/Projetos')
def Projeto():
    return 'Projetos'

#projeto para html

@app.route('/contatos')
def contatos():
    return render_template('contatos.html', titulo = 'Contatos')

#rota do sobre 

@app.route('/sobre')
def sobre():
    return render_template('sobre.html', titulo = 'Sobre')