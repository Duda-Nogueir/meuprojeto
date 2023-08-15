from app import app, db

class ContatoModel(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(40), nullable = False)
    email = db.Column(db.String(60), nullable = False)
    telefone = db.Column(db.String(14), nullable = False)
    mensagem = db.Column(db.Text, nullable = True)

    def __repr__(self):
        return 'Contato:'