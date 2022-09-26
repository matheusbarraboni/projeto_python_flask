from flask import Blueprint, render_template, request, redirect, url_for, flash
from ..extensions import db
from ..models.filme import Filme


filme_bp = Blueprint('filme_bp', __name__)


@filme_bp.route('/filme', methods=['GET'])
def tela_listar():
        
    db.create_all()
    filmes_cadastrados = Filme.query.order_by('status')
    return render_template('lista_filmes.html', filmes=filmes_cadastrados)


@filme_bp.route('/filme', methods=['POST'])
def cadastrar():
    # try:
    filme = Filme(
        nome = request.form['nome'],
        tamanho = request.form['tamanho'] or None,
        status = request.form['status'],
        genero = request.form['genero'],
        plataforma = request.form['plataforma'],
    )

    db.session.add(filme)
    db.session.commit()

    return redirect(url_for("filme_bp.tela_listar"))
    # except ReferenceError:
    #     flash("Algum campo não foi devidamente preenchido, tente novamente.")
    #     return redirect(request.url)
    # except :
    #     flash("Algo de errado aconteceu, tente novamente.")
    #     return redirect(request.url)


@filme_bp.route('/filme/create', methods=['GET'])
def tela_cadastrar():
    return render_template("criar_filme.html")

@filme_bp.route('/filme/delete/<filme_id>', methods=['GET'])
def tela_deletar(filme_id):
    filme = Filme.query.filter_by(id = filme_id).first()
    return render_template("confirma_deletar_filme.html", filme=filme)

@filme_bp.route('/filme/delete', methods=['POST'])
def deletar():
    id_filme = request.form['id']
    filme = Filme.query.filter_by(id = id_filme).first()
    db.session.delete(filme)
    db.session.commit()

    return redirect(url_for('filme_bp.tela_listar'))

@filme_bp.route('/filme/update/<filme_id>', methods=['GET'])
def tela_atualizar(filme_id):
    filme = Filme.query.filter_by(id = filme_id).first()
    return render_template('atualizar_filme.html', filme=filme)

@filme_bp.route('/filme/update', methods=['POST'])
def atualizar():
    filme = Filme.query.filter_by(id=request.form['id']).first()

    filme.nome = request.form['nome']
    filme.tamanho = request.form['tamanho']
    filme.status = request.form['status']
    filme.genero = request.form['genero']
    filme.plataforma = request.form['plataforma']

    db.session.add(filme)
    db.session.commit()

    return redirect(url_for('filme_bp.tela_listar'))