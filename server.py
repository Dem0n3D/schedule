from flask import Flask, render_template, redirect, url_for, jsonify

from alchemy import db

from models import *

app = Flask(__name__)
app.config.from_object('config')

db.init_app(app)

if __name__ == '__main__':
    app.run()
