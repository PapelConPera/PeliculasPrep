import os

from flask import Flask
app = Flask(__name__)

with app.app_context():
    from . import db
    db.init_app(app)


