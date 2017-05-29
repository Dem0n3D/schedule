from flask import Flask, render_template, redirect, url_for, jsonify

from alchemy import db

from models import *
from api import api_v1_bp
from views import index_bp

app = Flask(__name__)
app.config.from_object('config')

db.init_app(app)

app.register_blueprint(index_bp)
app.register_blueprint(api_v1_bp, url_prefix="/api/v1")

if __name__ == '__main__':
    app.run()
