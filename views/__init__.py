# -*- coding: utf_8 -*-
from flask import Blueprint
from flask import render_template

index_bp = Blueprint('index', __name__, template_folder="templates")


@index_bp.route('/')
def index():
    return render_template("index.html")

@index_bp.route('/', defaults={'path': ''})
@index_bp.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")
