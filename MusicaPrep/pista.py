from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from MusicaPrep.db import get_db

bp = Blueprint('pista', __name__, url_prefix='/pistas')

@bp.route('/')
def index():
    db = get_db()
    lista_pistas = db.execute(
        """SELECT name,composer
            FROM tracks
            ORDER BY name,composer"""
    ).fetchall()
    return render_template('pista.html', pista=lista_pistas)

@bp.route('/<int:id>/')
def update(id):
    db = get_db()
    lista_pistas = db.execute(
        """SELECT Title
            FROM albums
            ORDER BY Title"""
    ).fetchall()


    lista_nombreADefinir = db.execute(
        """SELECT name,composer
            FROM tracks
            ORDER BY name,composer"""
    ).fetchall()

    return render_template('blog/update.html', post=post)