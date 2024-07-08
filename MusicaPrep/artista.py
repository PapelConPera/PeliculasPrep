from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from MusicaPrep.db import get_db

bp = Blueprint('artista', __name__, url_prefix='/artistas')

@bp.route('/')
def index():
    db = get_db()
    lista_artistas = db.execute(
        """SELECT name,ArtistId
            FROM artists
            ORDER BY name"""
    ).fetchall()
    return render_template('artistas.html', artista=lista_artistas)


@bp.route('/<int:id>/')
def detalle(id):
    db = get_db()
    consulta = """
            SELECT name, ArtistId
            FROM artists
            WHERE ArtistId = ?"""

    resultado = db.execute(consulta, (id,))
    lista_artista= resultado.fetchone()


    pagina = render_template('detalleArtista.html', artista = lista_artista)

    return pagina