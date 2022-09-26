from ..extensions import db

class Filme(db.Model):
    __tablename__ = "filmes"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100))
    tamanho = db.Column(db.Integer)
    status = db.Column(db.String(20))
    genero = db.Column(db.String(30))
    plataforma = db.Column(db.String(30))

    def __repr__(self):
        return f"<Filme(nome={self.nome}, diretor={self.diretor}, status={self.status}, genero={self.genero}, plataforma{self.plataforma})>"
