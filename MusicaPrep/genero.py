from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from MusicaPrep.db import get_db

bp = Blueprint('genero', __name__, url_prefix='/generos')

@bp.route('/')
def index():
    db = get_db()
    lista_generos = db.execute(
        """SELECT name 
            FROM genres
            ORDER BY name"""
    ).fetchall()
    return render_template('genero.html', genero=lista_generos)