from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return "Hello world!"

@app.route('/saluto')
def saluto():
    studente = { 'nome': 'Andrea', 'cognome': 'Colleoni' }
    return render_template('saluto.html', studente=studente)