from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from MusicaPrep.db import get_db

bp = Blueprint('albun', __name__, url_prefix='/albums')

@bp.route('/')
def index():
    db = get_db()
    lista_albun = db.execute(
        """SELECT Title, AlbumId
            FROM albums
            ORDER BY Title"""
    ).fetchall()
    return render_template('albun.html', albun=lista_albun)


@bp.route('/<int:id>/')
def detalle(id):
    db = get_db()
    consulta1 = """
    SELECT Title, AlbumId 
    FROM albums
    WHERE AlbumId = ?"""

    resultado = db.execute(consulta1, (id,))
    lista_albums = resultado.fetchone()

    consulta2 = """  
            SELECT name, AlbumId
            FROM tracks
            WHERE AlbumId = ?"""
    
    resultado = db.execute(consulta2, (id,))
    lista_cancion = resultado.fetchall()
    

    pagina = render_template('detalleAlbum.html', album=lista_albums, cancion = lista_cancion)

    return pagina