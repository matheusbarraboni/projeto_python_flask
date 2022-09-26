from flask import Blueprint, render_template, request, redirect, url_for, flash
from ..extensions import db
from ..models.filme import Filme


filme_bp = Blueprint('filme_bp', __name__)


@filme_bp.route('/filme', methods=['GET'])
def listar_filmes_tela():
        
    db.create_all()
    filmes_cadastrados = Filme.query.all()
    return render_template('lista_filmes.html', filmes=filmes_cadastrados)


@filme_bp.route('/filme', methods=['POST'])
def cadastrar_filme():
    # try:
    print(request.args)
    filme = Filme(
        nome = request.form['nome'],
        tamanho = request.form['tamanho'] or None,
        status = request.form['status'],
        genero = request.form['genero'],
        plataforma = request.form['plataforma'],
    )

    db.session.add(filme)
    db.session.commit()

    return redirect(url_for("filme_bp.listar_filmes_tela"))
    # except ReferenceError:
    #     flash("Algum campo não foi devidamente preenchido, tente novamente.")
    #     return redirect(request.url)
    # except :
    #     flash("Algo de errado aconteceu, tente novamente.")
    #     return redirect(request.url)


@filme_bp.route('/filme/create', methods=['GET'])
def criar_filme_tela():
    return render_template("criar_filme.html")
