from app import app, db
from flask import render_template, url_for, request, flash
from app.forms import Contato
from app.models import ContatoModel
@app.route('/')
def index():
    return render_template('index.html',titulo = 'Página inicial')



# rota para projetos

@app.route('/Projetos')
def Projeto():
    return 'Projetos'

#projeto para html

@app.route('/contatos', methods=['POST', 'GET'])
def contatos():
    dados_formulario = None
    formulario = Contato()
    print('Acessou a rota contatos!')
    if formulario.validate_on_submit():
        flash('Esse formulário foi enviado com sucesso!')
        nome = formulario.nome.data
        email = formulario.email.data
        telefone = formulario.telefone.data
        mensagem = formulario.mensagem.data
        
        novo_contato = ContatoModel(nome=nome, email=email, telefone=telefone, mensagem=mensagem)
        db.session.add(novo_contato)
        db.session.commit()
        
    
        
    return render_template('contatos.html', titulo = 'Contatos',formulario = formulario,dados_formulario = dados_formulario)

#rota do sobre 

@app.route('/sobre')
def sobre():
    return render_template('sobre.html', titulo = 'Sobre')
