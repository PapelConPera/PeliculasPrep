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
        """SELECT Title
            FROM albums
            ORDER BY Title"""
    ).fetchall()
    return render_template('albun.html', albun=lista_albun)