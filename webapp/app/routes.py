from app import app
from flask import request, render_template

import random

@app.route('/')
@app.route('/index')
def index():
    return "Hello world!"

@app.route('/saluto')
def saluto():
    studente = { 'nome': 'Andrea', 'cognome': 'Colleoni' }
    return render_template('saluto.html', studente=studente)


@app.route('/casuali')
def casuali():
    list = []
    for i in range(0, 9):
        list.append(random.randint(1, 100))
    print(list)
    return render_template('casuali.html', numeri=list)

@app.route('/tabellina', methods=['GET', 'POST'])
def tabellina():
    if request.method == 'POST':
        numero = request.form.get('numero')
        ripetizioni = request.form.get('ripetizioni')

        print(numero, ripetizioni)
        list = []
        for i in range(1, int(ripetizioni) + 1):
            list.append(i * int(numero))
        return render_template('tabellina.html', numeri=list, numero=numero)

    elif request.method == 'GET':
        return render_template('tabellina.html')