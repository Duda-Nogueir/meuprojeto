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

@app.route('/projetos')
def projeto():
    return render_template('projetos.html', titulo = 'Projetos')